from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    locator_payment_information_label = (By.XPATH, "//div[text()='Payment Information:']")
    locator_shipping_information_label = (By.XPATH, "//div[text()='Shipping Information:']")
    locator_price_total_label = (By.XPATH, "//div[text()='Price Total']")
    locator_checkout_complete_label = (By.XPATH, "//span[text()='Checkout: Complete!']")
    locator_summary_value_label = (By.CLASS_NAME, "summary_value_label")
    locator_check_logo = (By.CLASS_NAME, "pony_express")
    locator_thank_you_message = (By.XPATH, "//h2[text()='Thank you for your order!']")
    locator_thank_you_message_text = (By.XPATH, "//h2[@class='complete-header']")
    locator_back_home_button = (By.ID, "back-to-products")
    locator_summary_subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
    locator_summary_tax_label = (By.CLASS_NAME, "summary_tax_label")
    locator_summary_total_label = (By.CLASS_NAME, "summary_total_label")
    locator_cancel_order_btn = (By.ID, "cancel")
    locator_finish_order_btn = (By.ID, "finish")
