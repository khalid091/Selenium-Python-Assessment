from selenium.webdriver.common.by import By

class CartPageLocators:
    locator_cart_title = (By.CLASS_NAME, "title")
    locator_cart_item_name = (By.CLASS_NAME, "inventory_item_name")
    locator_qty_label = (By.CLASS_NAME, "cart_quantity_label")
    locator_qty_desc_label = (By.CLASS_NAME, "cart_desc_label")
    locator_cart_qty = (By.CLASS_NAME, "cart_quantity")
    locator_cart_item = (By.CLASS_NAME, "cart_item")
    locator_continue_shopping_btn = (By.ID, "continue-shopping")
    locator_checkout_btn = (By.ID, "checkout")
    locator_checkout_first_name = (By.ID, "first-name")
    locator_checkout_last_name = (By.ID, "last-name")
    locator_checkout_postal_code = (By.ID, "postal-code")
    locator_checkout_continue_btn = (By.ID, "continue")