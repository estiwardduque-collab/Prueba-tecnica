import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.generators import Generators
from config.config import Config

class TestFullPurchaseFlow:
    def test_full_purchase_flow(self, driver):
        # 1. Register/Login (Need to be logged in for checkout address flow to be smoother or as per req)
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        home_page.go_to_register()
        
        email = Generators.generate_email()
        password = Generators.generate_password()
        first_name = Generators.generate_name()
        last_name = Generators.generate_last_name()
        
        register_page = RegisterPage(driver)
        register_page.register_user(first_name, last_name, email, password)
        
        # 2. Go Home & Select Product
        home_page.open_url(Config.BASE_URL)
        home_page.select_first_product()
        
        # 3. Add to Cart
        product_page = ProductPage(driver)
        product_page.add_to_cart()
        assert "Success: You have added" in product_page.get_success_message()
        
        # 4. Go to Cart
        product_page.go_to_cart()
        
        # 5. Proceed to Checkout
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()
        
        # 6. Checkout Flow
        checkout_page = CheckoutPage(driver)
        address_data = Generators.generate_address_data()
        
        checkout_page.fill_billing_details(address_data)
        checkout_page.process_checkout_steps()
        
        # 7. Validate
        final_msg = checkout_page.get_final_confirmation()
        assert "Your order has been placed!" in final_msg
