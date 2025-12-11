from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.ID, "input-telephone")
    PASSWORD = (By.ID, "input-password")
    CONFIRM_PASSWORD = (By.ID, "input-confirm")
    PRIVACY_POLICY = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content h1")

    def register_user(self, first_name, last_name, email, password):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.TELEPHONE, "123456789") # Generic phone
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)
        self.click(self.PRIVACY_POLICY)
        self.click(self.CONTINUE_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
