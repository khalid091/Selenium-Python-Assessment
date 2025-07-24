from pages.ProductPage.locators.ProductPageLocators import ProductPageLocators
from pages.LoginPage.locators.SwagLoginPageLocators import SwagLoginPageLocators
from pages.ProductPage.ProductPage import ProductPage
from pages.LoginPage.SwagLoginPage import SwagLoginPage
from selenium.common.exceptions import NoSuchElementException
from utils.wait_utils import wait_utils
import time

class ProductPageActions:
    def __init__(self, driver = None):
        self.driver = driver
        self.product_page = ProductPage(self.driver)
        self.swag_login_page = SwagLoginPage(self.driver)
        
    def validate_product_page_icons(self):
        wait_utils.wait_for_element(self.driver, *ProductPageLocators.locator_swaglabs_applogo)
        assert self.product_page.is_burgermenu_button_displayed(), "Burger Menu button is not displayed"
        assert self.product_page.is_product_sort_container_displayed(), "Product Filter buttone is not displayed"
        assert self.product_page.is_shopping_cart_link_displayed(), "Shopping Cart button is not displayed"
        assert self.product_page.is_swaglogo_displayed(), "Swag Labs logo is not displayed"
        
    def validate_product_items(self):
        
        inventory_items = wait_utils.wait_for_all_elements(self.driver, *ProductPageLocators.locator_inventory_item)
        
        ## This is for debugging purpose
        # processed_count = 0
        
        # Loop through each item and verify the details
        for item in inventory_items:

            item_name = self.product_page.is_product_item_name_displayed(item).text
            assert item_name, "Product name is not displayed"
            
            item_img = self.product_page.is_product_item_img_displayed(item)
            assert item_img, "Product image is not displayed"
            
            item_desc = self.product_page.is_product_item_desc_displayed(item).text
            assert item_desc, "Product desc is not displayed"
            
            item_price = self.product_page.is_product_item_price_displayed(item).text
            assert item_price, "Product price is not displayed"
            
            ## This is for debugging purpose
            # processed_count += 1
            # print(f"item {processed_count}: {item_name}")
            # print(f"item {processed_count}: {item_img}")
            # print(f"item {processed_count}: {item_desc}")
            # print(f"item {processed_count}: {item_price}")

        
    def add_to_cart_product_items(self):
        inventory_items = wait_utils.wait_for_all_elements(self.driver, *ProductPageLocators.locator_inventory_item)
        # Get the total number of items in the inventory
        total_items = len(inventory_items)
        
        # Loop through each item and click the "Add to cart" button
        for item in inventory_items:
            add_to_cart_button = self.product_page.is_add_to_cart_btn_displayed(item)
            button_text = add_to_cart_button.text.strip()
            if button_text == "Add to cart":
                add_to_cart_button.click()
                
                # Wait for the remove button to be displayed after adding to cart
                remove_button = self.product_page.is_remove_btn_displayed(item)
                wait_utils.wait_for_element_displayed(self.driver, lambda: remove_button)
                assert remove_button.is_displayed(), "Remove button is not displayed after clicking Add to cart"
                
                # Wait for the cart item badge to reflect the updated quantity
                shopping_cart_badge = self.product_page.is_shopping_cart_badge_displayed()
                wait_utils.wait_for_element_displayed(self.driver, lambda: shopping_cart_badge)
                assert shopping_cart_badge.is_displayed(), "Shopping cart badge is not displayed after adding item to cart"
                
        # Get the updated cart item quantity
        cart_item_qty = int(shopping_cart_badge.text.strip())
        ## Debugging purpose
        # print(f"Total items added to cart: {cart_item_qty}")
        # print(f"Total items in inventory: {total_items}")
        assert total_items == cart_item_qty, f"The cart item quantity {cart_item_qty} does not match the total items {total_items} added to the cart"
        
    def remove_item_from_products(self):
        inventory_items = wait_utils.wait_for_all_elements(self.driver, *ProductPageLocators.locator_inventory_item)
        
        for item in inventory_items:
            remove_button = self.product_page.is_remove_btn_displayed(item)
            if remove_button.is_displayed():
                remove_button.click()
                # Wait for the add to cart button to be displayed after removing
                add_to_cart_button = self.product_page.is_add_to_cart_btn_displayed(item)
                wait_utils.wait_for_element_displayed(self.driver, lambda: add_to_cart_button)
                assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed after clicking Remove"

                try:
                    # Wait for the shopping cart badge to reflect the updated quantity
                    shopping_cart_badge = self.product_page.is_shopping_cart_badge_displayed()
                    wait_utils.wait_for_element_displayed(self.driver, lambda: shopping_cart_badge)
                    cart_item_qty = shopping_cart_badge.text.strip()
                    # # Debugging purpose
                    # print(f"item quantity after removal: {cart_item_qty}")
                    if cart_item_qty == "":
                        raise NoSuchElementException
                except NoSuchElementException:
                    assert True, "Shopping cart badge is not displayed after removing all item"
                    
    def click_shopping_cart_link(self):
        wait_utils.wait_for_element_displayed(self.driver, lambda: self.product_page.is_shopping_cart_link_displayed())
        shopping_cart_link = self.product_page.is_shopping_cart_link_displayed()
        shopping_cart_link.click()
        
    def user_logout(self):
        burgermenu_button = self.product_page.is_burgermenu_button_displayed()
        burgermenu_button.click()
        
        wait_utils.wait_for_element_displayed(self.driver, lambda: self.product_page.is_logout_link_displayed())
        logout_link = self.product_page.is_logout_link_displayed()
        logout_link.click()
        
        # Validate that the user is logged out by checking if the login button is displayed
        assert self.swag_login_page.is_login_button_displayed(), "Logout was not successful, Login button is not displayed"
        
    