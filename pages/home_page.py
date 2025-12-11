from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//span[text()='My Account']")
    REGISTER_OPTION = (By.LINK_TEXT, "Register")
    LOGIN_OPTION = (By.LINK_TEXT, "Login")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    
    # Generic product selection locator (e.g., first element in list or specific one if needed)
    FIRST_PRODUCT_IMAGE = (By.CSS_SELECTOR, ".product-layout .image a")

    def go_to_register(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.REGISTER_OPTION)

    def go_to_login(self):
        self.click(self.MY_ACCOUNT_DROPDOWN)
        self.click(self.LOGIN_OPTION)

    def search_product(self, product_name):
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT_IMAGE)
