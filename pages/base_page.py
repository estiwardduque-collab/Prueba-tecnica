import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import Waits
from config.config import Config

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waits = Waits(driver)

    def handle_ssl_warning(self):
        """
        Detects 'Your connection is not private' or similar SSL warnings
        and tries to proceed by clicking 'Advanced' -> 'Proceed to ...'.
        """
        try:
            # Short wait to check title
            time.sleep(1) 
            title = self.driver.title.lower()
            
            # Common titles for SSL errors in different languages
            error_titles = ["privacy error", "error de privacidad", "privacidad", "not private", "no es privado"]
            
            if any(t in title for t in error_titles):
                print(f"SSL Warning detected. Title: {self.driver.title}")
                
                try:
                    advanced_btn = self.driver.find_element(By.ID, "details-button")
                    advanced_btn.click()
                    print("Clicked 'Advanced' button.")
                    time.sleep(0.5) 
                except NoSuchElementException:
                    pass

                try:
                    proceed_link = self.driver.find_element(By.ID, "proceed-link")
                    proceed_link.click()
                    print("Clicked 'Proceed' link.")
                except NoSuchElementException:
                    pass
        except Exception as e:
            print(f"Error handling SSL warning: {e}")

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.waits.wait_for_element_visible(locator)

    def click(self, locator):
        try:
            element = self.waits.wait_for_element_clickable(locator)
            element.click()
        except (TimeoutException, ElementClickInterceptedException):
            # Fallback for interception (e.g., banner) or timeout
            try:
                print(f"Click intercepted or timed out for {locator}. Attempting safe_click...")
                self.safe_click(locator)
            except Exception as e:
                self.take_screenshot("click_error")
                raise Exception(f"Element with locator {locator} not clickable. Error: {e}")

    def safe_click(self, locator):
        """
        Attempts to click an element safely by:
        1. Rescuing from ElementClickInterceptedException
        2. Removing known blocking elements (Bitnami banner)
        3. Scrolling to the element
        4. Retrying the click
        """
        try:
            element = self.waits.wait_for_element_present(locator) # Ensure presence first
            
            # Scroll to element
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5) # Give it a moment to settle

            # Remove Bitnami banner if present
            try:
                self.driver.execute_script("var banner = document.querySelector('#bitnami-banner'); if (banner) { banner.remove(); }")
                print("Removed Bitnami banner.")
            except Exception:
                pass # Script failed or banner not found, ignore

            # Wait until clickable
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            # Final attempt with JS click if standard click fails
            print(f"Standard click failed, trying JS click. Error: {e}")
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        try:
            element = self.waits.wait_for_element_visible(locator)
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            self.take_screenshot("type_error")
            raise Exception(f"Element with locator {locator} not found to likely type.")

    def get_text(self, locator):
        try:
            element = self.waits.wait_for_element_visible(locator)
            return element.text
        except TimeoutException:
            self.take_screenshot("get_text_error")
            raise

    def take_screenshot(self, name):
        if not os.path.exists(Config.SCREENSHOT_DIR):
            os.makedirs(Config.SCREENSHOT_DIR)
        filename = f"{Config.SCREENSHOT_DIR}/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
    
    def is_visible(self, locator):
        try:
            self.waits.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False
