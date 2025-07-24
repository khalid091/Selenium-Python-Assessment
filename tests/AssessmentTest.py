from actions.SwagLoginPageActions import SwagLoginPageActions
from actions.ProductPageActions import ProductPageActions
from actions.CartPageActions import CartPageActions
from actions.CheckoutPageActions import CheckoutPageActions
from actions.Common import Common
from utils.config import get_config
from utils.browser import get_driver
from utils.testdataprovider import get_cell_data
import unittest

class TestAssessment(unittest.TestCase):
    
    def setUp(self):
        
        # Config Instances
        self.config = get_config()
        self.driver = get_driver()
        if self.driver is None:
            raise RuntimeError("Failed to initialize WebDriver")
        
        # Object Instances
        self.swag_login_page_actions = SwagLoginPageActions(self.driver)
        self.product_page_actions = ProductPageActions(self.driver)
        self.cart_page_actions = CartPageActions(self.driver)
        self.checkout_page_actions = CheckoutPageActions(self.driver)
        self.common = Common(self.driver)
        
        # Variable Instances
        self.invalid_username = get_cell_data(2, "username")
        self.invalid_password = get_cell_data(2, "password")
        self.valid_username = get_cell_data(3, "username")
        self.valid_password = get_cell_data(3, "password")
        self.first_name = get_cell_data(3, "first_name")
        self.last_name = get_cell_data(3, "last_name")
        self.postal_code = get_cell_data(3, "postal_code")
        
    def test_validate_login_page_and_errors(self):
        """
            Test login page error handling:
            - Username required error
            - Password required error
            - Invalid credentials error
        """
        
        # Open the login page
        self.common.open_login_page()
        
        # Validate the login page elements
        self.swag_login_page_actions.validate_login_page_elements()
        
        # Verify the username required error
        self.swag_login_page_actions.enter_username_and_password('', self.invalid_password)
        self.swag_login_page_actions.click_login_button()
        self.swag_login_page_actions.verify_username_required_error()
        
        # Verify the password required error
        self.swag_login_page_actions.enter_username_and_password(self.invalid_username, '')
        self.swag_login_page_actions.click_login_button()
        self.swag_login_page_actions.verify_password_required_error()
        
        # Verify the invalid credentials error
        self.swag_login_page_actions.enter_username_and_password(self.invalid_username, self.invalid_password)
        self.swag_login_page_actions.click_login_button()
        self.swag_login_page_actions.verify_invalid_credentials_error()
        
    def test_validate_product_page_items(self):
        """
            Validate Product Home Page Elements:
            - Verify that headers and icons are displayed on the home page.
        """
        
        # Open the Login Page
        self.common.open_login_page()
        
        # Login the user
        self.swag_login_page_actions.enter_username_and_password(self.valid_username, self.valid_password)
        self.swag_login_page_actions.click_login_button()
        
        # Validate the product page elements
        self.product_page_actions.validate_product_page_icons()
        
    def test_add_and_remove_all_items_to_cart(self):
        """
            Add to Cart and Remove Item from Cart:
            - Add available products to the cart.
            - Remove products from the cart.
            - Verify that product items are displayed.
        """
        
        self.valid_username = get_cell_data(3, "username")
        self.valid_password = get_cell_data(3, "password")
        
        # Open the Login Page
        self.common.open_login_page()
        
        # Login the user
        self.swag_login_page_actions.enter_username_and_password(self.valid_username, self.valid_password)
        self.swag_login_page_actions.click_login_button()

        # Validate product items
        self.product_page_actions.validate_product_items()
        
        # Add all items to cart
        self.product_page_actions.add_to_cart_product_items()
        
        # Remove all items from product page
        self.product_page_actions.remove_item_from_products()
        
    def test_checkout_all_items(self):
        """
            Checkout all product items:
            - Validate the elements on the checkout pages.
            - Validate the total price and item count of the products checked out.
            - Ensure successful logout.
        """

        # Open the Login Page
        self.common.open_login_page()
        
        # Login the user
        self.swag_login_page_actions.enter_username_and_password(self.valid_username, self.valid_password)
        self.swag_login_page_actions.click_login_button()
        
        # Validate product items in Cart
        self.product_page_actions.add_to_cart_product_items()
        self.product_page_actions.click_shopping_cart_link()
        self.cart_page_actions.validate_cart_page()
        self.cart_page_actions.validate_cart_items()
        self.cart_page_actions.click_checkout()
        
        # Fill in the checkout information
        self.cart_page_actions.fill_checkout_info(self.first_name, self.last_name, self.postal_code)
        self.cart_page_actions.click_checkout_continue()
        
        # Validate the checkout overview price totals
        self.checkout_page_actions.validate_checkout_overview()
        self.checkout_page_actions.validate_total_price()
        self.checkout_page_actions.click_finish_order()
        self.checkout_page_actions.validate_checkout_complete_page()
        self.checkout_page_actions.click_back_home()
        self.product_page_actions.user_logout()
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
