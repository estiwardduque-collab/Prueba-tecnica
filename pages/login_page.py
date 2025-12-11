from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Login']")
    MY_ACCOUNT_HEADER = (By.CSS_SELECTOR, "#content h2:first-child")

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def is_login_successful(self):
        try:
            text = self.get_text(self.MY_ACCOUNT_HEADER)
            return "My Account" in text
        except:
            return False
