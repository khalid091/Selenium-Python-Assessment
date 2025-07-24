from pages.LoginPage.locators.SwagLoginPageLocators import SwagLoginPageLocators

class SwagLoginPage:
    def __init__(self, driver=None):
        self.driver = driver
    
    def is_username_input_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_username_input).is_displayed()
    
    def is_password_input_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_password_input).is_displayed()
    
    def is_login_button_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_login_button).is_displayed()

    def is_swaglabs_logo_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_swaglabs_logo).is_displayed()
    
    def is_invalid_credentials_error_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_invalid_credentials_error).is_displayed()
    
    def is_password_required_error_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_password_required_error).is_displayed()
    
    def is_username_required_error_displayed(self):
        return self.driver.find_element(*SwagLoginPageLocators.locator_username_required_error).is_displayed()