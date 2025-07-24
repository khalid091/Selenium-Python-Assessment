from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config import get_config


def get_driver():
    try:
        config = get_config()
        driver_path = config["driver_path"]

        options = Options()
        options.add_argument("--disable-features=PasswordManager")
        # options.add_argument("--headless")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--incognito")

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        print("WebDriver initialized successfully.")
        return driver
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return None
