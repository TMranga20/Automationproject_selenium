from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def remove_ads(self):        # Remove advertisement iframes that may interfere with interactions
        self.driver.execute_script("""
            var ads = document.querySelectorAll("iframe");
            ads.forEach(ad => ad.remove());
        """)

    def click(self, locator): # Wait for element to be clickable, scroll it into view, and click it, handling cases where element may be covered by ads or not immediately interactable
        self.remove_ads()

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_top(self): # Scroll to the top of the page to ensure elements are in view and not covered by sticky headers or ads
        self.driver.execute_script("window.scrollTo(0, 0);")

    def enter_text(self, locator, text): # Wait for element to be visible, clear it, and enter text, handling cases where element may not be interactable immediately
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator): # Wait for element to be visible and return its text, returning empty string if not found or not visible
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_displayed(self, locator):   # Check if element is visible on the page, returning False if not found or not visible   
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            return False
