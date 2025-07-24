from pages.ProductPage.locators.ProductPageLocators import ProductPageLocators

class ProductPage:
    def __init__(self, driver=None):
        self.driver = driver
        
    def is_swaglogo_displayed(self):
        return self.driver.find_element(*ProductPageLocators.locator_swaglabs_applogo)
    
    def is_burgermenu_button_displayed(self):
        return self.driver.find_element(*ProductPageLocators.locator_burgermenu_button)
    
    def is_shopping_cart_link_displayed(self):
        return self.driver.find_element(*ProductPageLocators.locator_shopping_cart_link)
    
    def is_product_sort_container_displayed(self):
        return self.driver.find_element(*ProductPageLocators.locator_product_sort_container)
    
    def is_product_item_name_displayed(self, item):
        return item.find_element(*ProductPageLocators.locator_item_name)
    
    def is_product_item_img_displayed(self, item):
        return item.find_element(*ProductPageLocators.locator_item_img)
    
    def is_product_item_desc_displayed(self, item):
        return item.find_element(*ProductPageLocators.locator_item_desc)
    
    def is_product_item_price_displayed(self, item):
        return item.find_element(*ProductPageLocators.locator_item_price)
    
    def is_add_to_cart_btn_displayed(self, item):
        return item.find_element(*ProductPageLocators.locator_add_to_cart_btn)
    
    def is_remove_btn_displayed(self, item):
        return item.find_element(*ProductPageLocators.locator_remove_btn)
    
    def is_shopping_cart_badge_displayed(self):
        return self.driver.find_element(*ProductPageLocators.locator_shopping_cart_badge)
    
    def is_logout_link_displayed(self):
        return self.driver.find_element(*ProductPageLocators.locator_logout_link)