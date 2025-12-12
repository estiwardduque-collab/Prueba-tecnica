import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.generators import Generators
from config.config import Config

class TestRegister:
    def test_register_new_user(self, driver):
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        home_page.go_to_register()

        register_page = RegisterPage(driver)
        first_name = Generators.generate_name()
        last_name = Generators.generate_last_name()
        email = Generators.generate_email()
        password = Generators.generate_password()

        register_page.register_user(first_name, last_name, email, password)
        
        message = register_page.get_success_message()
        assert "Account" in message, f"Expected success message to contain 'Account', but got: {message}"
