from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class SignupPage(BasePage): # Page Object Model class for the Signup page, containing locators and methods specific to signup interactions
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    NEW_USER_HEADER = (By.XPATH, "//*[contains(normalize-space(.),'New User Signup!')]")
    ACCOUNT_INFO_HEADER = (By.XPATH, "//b[contains(normalize-space(.),'Enter Account Information')]")
    EXISTING_EMAIL_ERROR = (By.XPATH, "//p[contains(normalize-space(.),'already exist')]")

    def is_signup_form_visible(self): # Check if the signup form is visible by verifying the presence of name, email fields, and signup button
        return (
            self.is_displayed(self.SIGNUP_NAME)
            and self.is_displayed(self.SIGNUP_EMAIL)
            and self.is_displayed(self.SIGNUP_BUTTON)
        )

    def enter_signup_name(self, name): # Enter the name into the signup name field, waiting for it to be visible and interactable before sending keys
        self.enter_text(self.SIGNUP_NAME, name)

    def enter_signup_email(self, email): # Enter the email into the signup email field, waiting for it to be visible and interactable before sending keys
        self.enter_text(self.SIGNUP_EMAIL, email)

    def click_signup(self): # Click the signup button, waiting for it to be clickable and handling potential cases where it may be covered by ads or not immediately interactable
        self.click(self.SIGNUP_BUTTON)

    def signup(self, name, email): # Perform the complete signup action by entering the name and email, and clicking the signup button
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.click_signup()

    def get_signup_name_value(self): # Retrieve the current value of the signup name field, waiting for it to be present and returning its value attribute
        element = self.wait.until(EC.presence_of_element_located(self.SIGNUP_NAME))
        return element.get_attribute("value")

    def get_signup_email_value(self): # Retrieve the current value of the signup email field, waiting for it to be present and returning its value attribute
        element = self.wait.until(EC.presence_of_element_located(self.SIGNUP_EMAIL))
        return element.get_attribute("value")

    def get_signup_name_validation_message(self): # Retrieve the validation message for the signup name field, waiting for it to be present and using JavaScript to get the validationMessage property, returning an empty string if not found
        element = self.wait.until(EC.presence_of_element_located(self.SIGNUP_NAME))
        return self.driver.execute_script("return arguments[0].validationMessage;", element) or ""

    def get_signup_email_validation_message(self): # Retrieve the validation message for the signup email field, waiting for it to be present and using JavaScript to get the validationMessage property, returning an empty string if not found
        element = self.wait.until(EC.presence_of_element_located(self.SIGNUP_EMAIL))
        return self.driver.execute_script("return arguments[0].validationMessage;", element) or ""

    def is_account_info_page_loaded(self): # Check if the account information page is loaded by verifying the presence of the account info header, with a fallback to checking the URL pattern if the header is not found within the timeout
        try:
            self.wait.until(EC.url_contains("/signup"))
            return self.is_displayed(self.ACCOUNT_INFO_HEADER)
        except TimeoutException:
            return False

    def get_existing_email_error(self): # Retrieve the error message displayed when trying to sign up with an existing email, waiting for it to be visible and returning its text, or an empty string if not found
        try:
            return self.get_text(self.EXISTING_EMAIL_ERROR)
        except TimeoutException:
            return ""
