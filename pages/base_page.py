import os
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.waits import Waits
from config.config import Config

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.waits = Waits(driver)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.waits.wait_for_element_visible(locator)

    def click(self, locator):
        try:
            element = self.waits.wait_for_element_clickable(locator)
            element.click()
        except TimeoutException:
            self.take_screenshot("click_error")
            raise Exception(f"Element with locator {locator} not clickable.")

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
