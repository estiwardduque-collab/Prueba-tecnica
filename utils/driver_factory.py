from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config import Config

class DriverFactory:
    @staticmethod
    def get_driver():
        if Config.BROWSER.lower() == "chrome":
            options = Options()
            if Config.HEADLESS_MODE:
                options.add_argument("--headless")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            return driver
        else:
            raise ValueError(f"Browser {Config.BROWSER} not supported yet.")
