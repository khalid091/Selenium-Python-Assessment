from pages.CheckoutPage.CheckoutPage import CheckoutPage
from pages.CheckoutPage.locator.CheckoutPageLocator import CheckoutPageLocators
from pages.ProductPage.ProductPage import ProductPage
from actions.CartPageActions import CartPageActions
from actions.CartPageActions import CartPageLocators
from utils.wait_utils import wait_utils
from utils.testdataprovider import get_cell_data

class CheckoutPageActions:
    def __init__(self, driver=None):
        self.driver = driver
        self.checkout_page = CheckoutPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPageActions(self.driver)
        
    def validate_checkout_overview(self):
        
        # Validate the checkout overview product items
        self.cart_page.validate_cart_items()
        
        shipping_info = get_cell_data(3, "shipping_information")
        payment_info = get_cell_data(3, "payment_information")
        
        summary_value_elements = wait_utils.wait_for_all_elements(self.driver, *CheckoutPageLocators.locator_summary_value_label)
        summary_values = []
        
        for element in summary_value_elements:
            summary_values.append(element.text.strip())
         
        assert self.checkout_page.is_summary_value_label_displayed(), "Summary value label is not displayed" 
        # print(f"Payment Info: {summary_values[0]}, Shipping Info: {summary_values[1]}")
        assert summary_values[0] == payment_info, "Payment information values does not match"   
        assert summary_values[1] == shipping_info, "Shipping information values does not match"
        
        # Heading labels           
        assert self.checkout_page.is_payment_info_label_displayed(), "Payment information label is not displayed"
        assert self.checkout_page.is_shipping_info_label_displayed(), "Shipping information label is not displayed"
        assert self.checkout_page.is_price_total_label_displayed(), "Price total label is not displayed"
        
        # Summary labels
        assert self.checkout_page.is_summary_subtotal_label_displayed(), "Summary subtotal label is not displayed"
        assert self.checkout_page.is_summary_total_label_displayed(), "Summary total label is not displayed"
        assert self.checkout_page.is_summary_tax_label_displayed(), "Summary tax label is not displayed"
        
        # Buttons
        assert self.checkout_page.is_cancel_order_btn_displayed(), "Cancel order button is not displayed"
        assert self.checkout_page.is_finish_order_btn_displayed(), "Finish order button is not displayed"
        
    def validate_total_price(self):
        
        cart_items = wait_utils.wait_for_all_elements(self.driver, *CartPageLocators.locator_cart_item)
        
        item_total_price = 0 # Counter
        
        for item in cart_items:
            item_price = self.product_page.is_product_item_price_displayed(item).text
            assert item_price, "Product price is not displayed"
            
            item_price = item_price.replace('$', '').strip() # Removing the dollar sign and converting to float for calculation
            item_total_price += float(item_price) # Adding the item price to the total price
            
            ##Debugging purpose
            # print(f"Item Price: {item_price}")
            # print(f"Total Price Before Addition: {total_price}")
            
        subtotal_price = self.checkout_page.is_summary_subtotal_label_displayed().text # Getting the expected subtotal price from the summary label
        subtotal_price = subtotal_price.replace('Item total: $', '').strip() # Removing the dollar sign and item total text
        assert float(subtotal_price) == item_total_price, "Subtotal price does not match total price"
        
        tax_price = self.checkout_page.is_summary_tax_label_displayed().text # Getting the expected tax price from the summary label
        tax_price = tax_price.replace('Tax: $', '').strip() # Removing the dollar sign and tax text
        
        expected_total_price = self.checkout_page.is_summary_total_label_displayed().text # Getting the expected total price from the summary label
        expected_total_price = expected_total_price.replace('Total: $', '').strip() # Removing the dollar sign and total text
        
        assert float(tax_price) + item_total_price == float(expected_total_price), "Total price does not match the sum of subtotal and tax"
        # Debugging purpose
        # print (f"Total Price: {expected_total_price}, Subtotal Price: {subtotal_price}, Tax Price: {tax_price}")
        
    def click_finish_order(self):
        finish_order_button = self.checkout_page.is_finish_order_btn_displayed()
        finish_order_button.click()
        
    def validate_checkout_complete_page(self):
        wait_utils.wait_for_element(self.driver, *CheckoutPageLocators.locator_check_logo)
        assert self.checkout_page.is_checkout_complete_label_displayed(), "Checkout complete label is not displayed"
        assert self.checkout_page.is_check_logo_displayed(), "Check logo is not displayed"
        assert self.checkout_page.is_thank_you_message_displayed(), "Thank you message is not displayed"
        assert self.checkout_page.is_thank_you_message_text_displayed(), "Thank you message text is not displayed"
        assert self.checkout_page.is_back_home_button_displayed(), "Back home button is not displayed"
        
    def click_back_home(self):
        back_home_button = self.checkout_page.is_back_home_button_displayed()
        back_home_button.click()