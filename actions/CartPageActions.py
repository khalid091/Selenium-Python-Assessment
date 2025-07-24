from pages.CartPage.CartPage import CartPage
from pages.CartPage.locators.CartPageLocators import CartPageLocators
from pages.ProductPage.ProductPage import ProductPage
from utils.wait_utils import wait_utils

class CartPageActions:
    def __init__(self, driver=None):
        self.driver = driver
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)
        
    def validate_cart_page(self):
        assert self.cart_page.is_cart_title_displayed(), "Cart title is not displayed"
        assert self.cart_page.is_qty_label_displayed(), "Quantity label is not displayed"
        assert self.cart_page.is_qty_desc_label_displayed(), "Quantity description label is not displayed"
        assert self.cart_page.is_continue_shopping_btn_displayed(), "Continue shopping button is not displayed"
        assert self.cart_page.is_checkout_btn_displayed(), "Checkout button is not displayed"
        
    def validate_cart_items(self):    
        cart_items = wait_utils.wait_for_all_elements(self.driver, *CartPageLocators.locator_cart_item)
        
        for item in cart_items:
            item_qty = self.cart_page.is_cart_qty_displayed(item)
            assert item_qty, "Cart item quantity is not displayed"
            
            item_name = self.cart_page.is_cart_item_name_displayed(item).text
            assert item_name, "Product name is not displayed"
            
            item_desc = self.product_page.is_product_item_desc_displayed(item).text
            assert item_desc, "Product desc is not displayed"
            
            item_price = self.product_page.is_product_item_price_displayed(item).text
            assert item_price, "Product price is not displayed"
            
    def click_continue_shopping(self):
        continue_shopping_button = self.cart_page.is_continue_shopping_btn_displayed()
        continue_shopping_button.click()
        
    def click_checkout(self):
        checkout_button = self.cart_page.is_checkout_btn_displayed()
        checkout_button.click()
        
    def click_checkout_continue(self):
        checkout_continue_button = self.cart_page.is_checkout_continue_btn_displayed()
        checkout_continue_button.click()
        
    def fill_checkout_info(self, first_name, last_name, postal_code):
        first_name_input = self.cart_page.is_checkout_first_name_displayed()
        last_name_input = self.cart_page.is_checkout_last_name_displayed()
        postal_code_input = self.cart_page.is_checkout_postal_code_displayed()

        assert self.cart_page.is_checkout_first_name_displayed(), "Checkout first name field is not displayed"
        assert self.cart_page.is_checkout_last_name_displayed(), "Checkout last name field is not displayed"
        assert self.cart_page.is_checkout_postal_code_displayed(), "Checkout postal code field is not displayed"
        
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)
        
    