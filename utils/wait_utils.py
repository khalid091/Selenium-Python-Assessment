from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Callable

class wait_utils:
    @staticmethod
    def wait_for_all_elements(driver, by: str, locator: str, timeout: int = 10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_all_elements_located((by, locator)))

    @staticmethod
    def wait_for_element(driver, by: str, locator: str, timeout: int = 10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located((by, locator)))

    @staticmethod
    def wait_for_element_displayed(driver, get_element_func: Callable, timeout: int = 10):
        WebDriverWait(driver, timeout).until(
            EC.visibility_of(get_element_func())
        )
