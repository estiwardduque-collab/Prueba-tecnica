from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    CART_TOTAL_BUTTON = (By.ID, "cart-total")
    VIEW_CART_LINK = (By.LINK_TEXT, "View Cart")
    
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_ALERT)

    def go_to_cart(self):
        # Sometimes the cart button needs a moment to update or the dropdown might need a click
        self.click(self.CART_TOTAL_BUTTON)
        self.click(self.VIEW_CART_LINK)
