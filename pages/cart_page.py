from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage): # Page Object Model class for the Cart page, containing locators and methods specific to cart interactions

    CART_PRODUCT = (By.XPATH, "//td[@class='cart_description']")

    def is_product_in_cart(self):
        return self.is_displayed(self.CART_PRODUCT)
