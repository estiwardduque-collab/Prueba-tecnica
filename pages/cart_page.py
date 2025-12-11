from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")
    CONTENT_HEADER = (By.CSS_SELECTOR, "#content h1")

    def proceed_to_checkout(self):
        # Ensure we are on the cart page
        self.waits.wait_for_url_contains("checkout/cart")
        self.click(self.CHECKOUT_BUTTON)
