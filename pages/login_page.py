from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage): # Page Object Model class for the Login page, containing locators and methods specific to login interactions

    EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    ERROR_MSG = (By.XPATH, "//p[contains(text(),'incorrect')]")

    def open(self): # Open the login page by navigating to the login URL
        self.driver.get("https://automationexercise.com/login")

    def login(self, email, password): # Perform the login action by entering the email and password, and clicking the login button
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self): # Retrieve the error message displayed on the login page after a failed login attempt
        return self.get_text(self.ERROR_MSG)
