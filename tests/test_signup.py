import time
from pages.home_page import HomePage
from pages.signup_page import SignupPage


def _unique_email():
    return f"signup_{int(time.time() * 1000)}@mailinator.com"


def test_signup_form_visible_on_login_page(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    assert signup.is_signup_form_visible()


def test_signup_name_field_accepts_input(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.enter_signup_name("Test User")
    assert signup.get_signup_name_value() == "Test User"


def test_signup_email_field_accepts_input(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.enter_signup_email("user@example.com")
    assert signup.get_signup_email_value() == "user@example.com"


def test_signup_empty_name_shows_native_validation(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.signup("", "validuser@example.com")
    assert signup.get_signup_name_validation_message() != ""


def test_signup_empty_email_shows_native_validation(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.signup("Valid User", "")
    assert signup.get_signup_email_validation_message() != ""


def test_signup_invalid_email_shows_native_validation(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.signup("Valid User", "not-an-email")
    assert signup.get_signup_email_validation_message() != ""


def test_signup_with_valid_data_navigates_to_account_info(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.signup("Fresh User", _unique_email())
    assert signup.is_account_info_page_loaded()


def test_signup_with_valid_data_changes_url_to_signup(setup):
    home = HomePage(setup)
    home.go_to_login()
    signup = SignupPage(setup)
    signup.signup("Another User", _unique_email())
    assert "/signup" in setup.current_url
