import pytest
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from utils.generators import Generators
from config.config import Config

class TestLogin:
    def test_login_user(self, driver):
        # Pre-condition: Create a user first so we can login with it
        # In a real scenario, we might use API or DB to seed data, but here we do it via UI or use a fixed one if allowed.
        # Required flow says: "Iniciar sesión con la cuenta creada", implying we create one in this test or rely on previous state.
        # Since state is not shared between tests in default pytest, we create a user in this test first.
        
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        home_page.go_to_register()
        
        email = Generators.generate_email()
        password = Generators.generate_password()
        
        register_page = RegisterPage(driver)
        register_page.register_user(Generators.generate_name(), Generators.generate_last_name(), email, password)
        
        # Logout to test login
        # Usually checking out logic or just navigating to login if session persists?
        # After register, OpenCart logs you in automatically.
        # So we should logout first.
        driver.delete_all_cookies() 
        home_page.open_url(Config.BASE_URL) 
        
        home_page.go_to_login()
        
        login_page = LoginPage(driver)
        login_page.login(email, password)
        
        assert login_page.is_login_successful(), "Login was not successful"
