from pages.CheckoutPage.locator.CheckoutPageLocator import CheckoutPageLocators

class CheckoutPage:
    def __init__(self, driver=None):
        self.driver = driver
    
    def is_summary_total_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_summary_total_label)
        
    def is_payment_info_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_payment_information_label)
    
    def is_shipping_info_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_shipping_information_label)
    
    def is_price_total_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_price_total_label)
    
    def is_summary_value_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_summary_value_label)
    
    def is_summary_subtotal_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_summary_subtotal_label)
    
    def is_summary_tax_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_summary_tax_label)
    
    def is_cancel_order_btn_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_cancel_order_btn)
    
    def is_finish_order_btn_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_finish_order_btn)
    
    def is_checkout_complete_label_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_checkout_complete_label)
    
    def is_check_logo_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_check_logo)
    
    def is_thank_you_message_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_thank_you_message)
    
    def is_thank_you_message_text_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_thank_you_message_text)
    
    def is_back_home_button_displayed(self):
        return self.driver.find_element(*CheckoutPageLocators.locator_back_home_button)
    