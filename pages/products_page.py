from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class ProductsPage(BasePage):

    FIRST_PRODUCT = (By.XPATH, "(//a[contains(@href,'/product_details/')])[1]")
    PRODUCT_TITLE = (By.XPATH, "//div[@class='product-information']/h2")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(@class,'cart') and contains(normalize-space(.),'Add to cart')]")
    CONTINUE_SHOPPING = (By.XPATH, "//button[@data-dismiss='modal' and contains(normalize-space(.),'Continue Shopping')]")

    def __init__(self, driver):
        super().__init__(driver)

    def _open_product_link(self, locator):
        self.scroll_to_top()
        element = self.wait.until(EC.presence_of_element_located(locator)) # Prefer navigating via href (more stable than click + ad overlays/new-tabs)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        href = element.get_attribute("href")
        if href and "/product_details/" in href:
            self.driver.get(href)
            return

        
        count_before = len(self.driver.window_handles) # Fallback: click and handle links that open in a new window/tab.
        self.click(locator)
        try:
            self.wait.until(EC.number_of_windows_to_be(count_before + 1))
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except TimeoutException:
            pass

    def view_product_by_index(self, index: int):
        if index < 1:
            raise ValueError("index must be 1-based (>= 1)")

        # Prefer a scoped locator; fall back to legacy absolute indexing used by FIRST_PRODUCT.
        candidates = [ 
            (By.XPATH, f"(//div[contains(@class,'features_items')]//a[contains(@href,'/product_details/')])[{index}]"),
            (By.XPATH, f"(//a[contains(@href,'/product_details/')])[{index + 3}]"),
            (By.XPATH, f"(//a[contains(@href,'/product_details/')])[{index}]"),
        ]

        last_error = None
        for locator in candidates:
            try:
                self._open_product_link(locator)
                return
            except Exception as exc:
                last_error = exc

        if last_error:
            raise last_error

    def view_first_product(self):
        self._open_product_link(self.FIRST_PRODUCT)

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def is_product_page_loaded(self):
        try:
            self.wait.until(lambda d: len(d.find_elements(*self.PRODUCT_TITLE)) > 0)
            elements = self.driver.find_elements(*self.PRODUCT_TITLE) or []
            return any(el.is_displayed() for el in elements)
        except TimeoutException:
            try: # Fallback: check URL pattern
                return bool(self.wait.until(EC.url_contains("/product_details/")))
            except TimeoutException:
                return False
