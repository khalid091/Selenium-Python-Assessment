from pages.LoginPage.locators.SwagLoginPageLocators import SwagLoginPageLocators
from selenium.webdriver.common.keys import Keys
from pages.LoginPage.SwagLoginPage import SwagLoginPage
from utils.wait_utils import wait_utils

class SwagLoginPageActions:
    def __init__(self, driver = None):
        self.driver = driver
        self.swag_login_page = SwagLoginPage(self.driver)
        
    def enter_username_and_password(self, username, password):
        username_input = self.driver.find_element(*SwagLoginPageLocators.locator_username_input)
        username_input.send_keys(Keys.CONTROL + 'a')  # Select all text
        username_input.send_keys(Keys.DELETE)  # Clear the input
        username_input.send_keys(username)
        password_input = self.driver.find_element(*SwagLoginPageLocators.locator_password_input)
        password_input.send_keys(Keys.CONTROL + 'a')  # Select all text
        password_input.send_keys(Keys.DELETE)  # Clear the input
        password_input.send_keys(password)
        
    def click_login_button(self):
        login_button = self.driver.find_element(*SwagLoginPageLocators.locator_login_button)
        login_button.click()
        
    def validate_login_page_elements(self):
        wait_utils.wait_for_element(self.driver, *SwagLoginPageLocators.locator_swaglabs_logo)
        assert self.swag_login_page.is_username_input_displayed(), "Username input is not displayed"
        assert self.swag_login_page.is_password_input_displayed(), "Password input is not displayed"
        assert self.swag_login_page.is_login_button_displayed(), "Login button is not displayed"
        assert self.swag_login_page.is_swaglabs_logo_displayed(), "SwagLabs logo is not displayed"
        
    def verify_username_required_error(self):
        wait_utils.wait_for_element(self.driver, *SwagLoginPageLocators.locator_username_required_error)
        assert self.swag_login_page.is_username_required_error_displayed(), "Username required error is not displayed"
    
    def verify_password_required_error(self):
        wait_utils.wait_for_element(self.driver, *SwagLoginPageLocators.locator_password_required_error)
        assert self.swag_login_page.is_password_required_error_displayed(), "Password required error is not displayed"
    
    def verify_invalid_credentials_error(self):
        wait_utils.wait_for_element(self.driver, *SwagLoginPageLocators.locator_invalid_credentials_error)
        assert self.swag_login_page.is_invalid_credentials_error_displayed(), "Invalid credentials error is not displayed"