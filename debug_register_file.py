from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.generators import Generators
from config.config import Config
import time

def debug_register():
    driver = DriverFactory.get_driver()
    try:
        home_page = HomePage(driver)
        home_page.open_url(Config.BASE_URL)
        home_page.go_to_register()
        
        first_name = Generators.generate_name()
        last_name = Generators.generate_last_name()
        email = Generators.generate_email()
        password = Generators.generate_password()

        register_page = RegisterPage(driver)
        register_page.register_user(first_name, last_name, email, password)
        
        message = register_page.get_success_message()
        with open("debug_msg.txt", "w", encoding="utf-8") as f:
            f.write(message)

    except Exception as e:
        with open("debug_msg.txt", "w", encoding="utf-8") as f:
            f.write(f"ERROR: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_register()
