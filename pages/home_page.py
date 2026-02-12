from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage: # Page Object Model class for the Home page, containing locators and methods specific to home page interactions

    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    LOGOUT_LINK = (By.XPATH, "//a[@href='/logout']")

    def __init__(self, driver): # Initialize the HomePage with the WebDriver instance and set up a WebDriverWait for handling dynamic content and potential Google vignette redirects
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def handle_google_vignette(self): # Handle potential Google vignette ad redirects by checking the current URL and navigating back to the home page if detected
        if "google_vignette" in self.driver.current_url:
            self.driver.get("https://automationexercise.com")

    def go_to_products(self): # Navigate to the Products page by clicking the products link, handling potential Google vignette redirects, and waiting for the URL to confirm navigation
        element = self.wait.until(
            EC.presence_of_element_located(self.PRODUCTS_LINK)
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.handle_google_vignette()
        self.wait.until(EC.url_contains("products"))

    def go_to_cart(self): # Navigate to the Cart page by clicking the cart link, handling potential Google vignette redirects, and waiting for the URL to confirm navigation
        element = self.wait.until(
            EC.presence_of_element_located(self.CART_LINK)
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.handle_google_vignette()
        self.wait.until(EC.url_contains("view_cart"))

    def go_to_login(self): # Navigate to the Login page by clicking the login link, handling potential Google vignette redirects, and waiting for the URL to confirm navigation
        element = self.wait.until(
            EC.presence_of_element_located(self.LOGIN_LINK)
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.handle_google_vignette()
        self.wait.until(EC.url_contains("login"))

    def logout(self): # Log out of the application by clicking the logout link, handling potential Google vignette redirects, and waiting for the URL to confirm navigation back to the login page
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.LOGOUT_LINK)
            )
            self.driver.execute_script("arguments[0].click();", element)
            self.handle_google_vignette()
            self.wait.until(EC.url_contains("login"))
        except TimeoutException:  # Fallback for sessions that are not authenticated.
            self.go_to_login()


