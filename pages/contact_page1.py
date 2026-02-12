# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage


# class ContactPage(BasePage):

#     CONTACT_LINK = (By.XPATH, "//a[text()=' Contact us']")
#     NAME = (By.NAME, "name")
#     EMAIL = (By.NAME, "email")
#     MESSAGE = (By.NAME, "message")
#     SUBMIT = (By.NAME, "submit")
#     SUCCESS = (By.XPATH, "//div[contains(text(),'Success')]")

#     def open_contact(self):
#         self.click(self.CONTACT_LINK)

#     def submit_form(self, name, email, message):
#         self.type(self.NAME, name)
#         self.type(self.EMAIL, email)
#         self.type(self.MESSAGE, message)
#         self.click(self.SUBMIT)

#     def is_success(self):
#         return self.is_visible(self.SUCCESS)
