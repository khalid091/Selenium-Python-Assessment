from pages.CartPage.locators.CartPageLocators import CartPageLocators

class CartPage:
    def __init__(self, driver=None):
        self.driver = driver
        
    def is_cart_title_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_cart_title)
    
    def is_qty_label_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_qty_label)
    
    def is_qty_desc_label_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_qty_desc_label)   
    
    def is_cart_qty_displayed(self, item):
        return item.find_element(*CartPageLocators.locator_cart_qty)
    
    def is_continue_shopping_btn_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_continue_shopping_btn)    
    
    def is_checkout_btn_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_checkout_btn)
    
    def is_cart_item_name_displayed(self, item):
        return item.find_element(*CartPageLocators.locator_cart_item_name)
    
    def is_checkout_first_name_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_checkout_first_name)
    
    def is_checkout_last_name_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_checkout_last_name)
    
    def is_checkout_postal_code_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_checkout_postal_code)
    
    def is_checkout_continue_btn_displayed(self):
        return self.driver.find_element(*CartPageLocators.locator_checkout_continue_btn)
    