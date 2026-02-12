from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_logout(driver):
    login = LoginPage(driver)
    home = HomePage(driver)

    login.open()
    login.login("valid@gmail.com", "valid123")
    home.logout()

    assert "login" in driver.current_url.lower()
