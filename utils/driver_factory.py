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
            
            # Additional stability options
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            
            # SSL and Security bypass
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--allow-insecure-localhost")
            options.add_argument("--ignore-ssl-errors=yes")
            options.add_argument("--disable-web-security")
            options.add_argument("--disable-site-isolation-trials")
            
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(Config.IMPLICIT_WAIT)
            return driver
        else:
            raise ValueError(f"Browser {Config.BROWSER} not supported yet.")
