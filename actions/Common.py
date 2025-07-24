from utils.config import get_config
from selenium.webdriver.common.by import By
import time

class Common:
    def __init__(self, driver = None):
        self.driver = driver
        self.config = get_config()
        
    def open_login_page(self):
        self.driver.get(self.config["base_url"])
        self.driver.delete_all_cookies()
        time.sleep(1)  # Wait for the page to load completely