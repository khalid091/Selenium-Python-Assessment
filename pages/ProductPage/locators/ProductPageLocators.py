from selenium.webdriver.common.by import By

class ProductPageLocators:
    locator_swaglabs_applogo = (By.CLASS_NAME, "app_logo")
    locator_burgermenu_button = (By.ID, "react-burger-menu-btn")
    locator_shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
    locator_product_sort_container = (By.CLASS_NAME, "product_sort_container")
    locator_inventory_item = (By.CLASS_NAME, "inventory_item")
    locator_item_name = (By.CLASS_NAME, "inventory_item_name ")
    locator_item_img = (By.CLASS_NAME, "inventory_item_img")
    locator_item_desc = (By.CLASS_NAME, "inventory_item_desc")
    locator_item_price = (By.CLASS_NAME, "inventory_item_price")
    locator_add_to_cart_btn = (By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
    locator_remove_btn = (By.CSS_SELECTOR, "button.btn.btn_secondary.btn_small.btn_inventory")
    locator_shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    locator_logout_link = (By.ID, "logout_sidebar_link")