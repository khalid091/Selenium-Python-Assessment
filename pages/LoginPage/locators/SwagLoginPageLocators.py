from selenium.webdriver.common.by import By

class SwagLoginPageLocators:
    locator_swaglabs_logo = (By.CLASS_NAME, "login_logo")
    locator_username_input = (By.NAME, "user-name")
    locator_password_input = (By.NAME, "password")
    locator_login_button = (By.ID, "login-button")
    locator_invalid_credentials_error = (By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']")
    locator_password_required_error = (By.XPATH, "//h3[text()='Epic sadface: Password is required']")
    locator_username_required_error = (By.XPATH, "//h3[text()='Epic sadface: Username is required']")