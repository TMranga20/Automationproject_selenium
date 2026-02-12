from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_invalid_login(setup):
    home = HomePage(setup)
    home.go_to_login()
    login = LoginPage(setup)
    login.login("wrong@test.com", "12345")
    assert "incorrect" in login.get_error_message()

def test_empty_login(setup):
    home = HomePage(setup)
    home.go_to_login()
    login = LoginPage(setup)
    login.login("", "")
    assert "Login" in setup.page_source

def test_password_only(setup):
    home = HomePage(setup)
    home.go_to_login()
    login = LoginPage(setup)
    login.login("", "123")
    assert "Login" in setup.page_source

def test_email_only(setup):
    home = HomePage(setup)
    home.go_to_login()
    login = LoginPage(setup)
    login.login("test@test.com", "")
    assert "Login" in setup.page_source

def test_login_page_title(setup):
    home = HomePage(setup)
    home.go_to_login()
    assert "Login" in setup.title
