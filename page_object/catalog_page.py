from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class CatalogPage(BasePage):
    CATALOG_PAGE_URL = "https://demo.opencart.com/index.php?route=product/category&path=20"
    DISPLAY_CONTROL = (By.ID, 'display-control')
    PRODUCT_LIST = (By.ID, 'product-list')
    PRODUCT_THUMB = (By.CLASS_NAME, 'product-thumb')
    DESCRIPTION = (By.CLASS_NAME, 'description')
    PRICE = (By.CLASS_NAME, 'price')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[onclick*="cart.add"]')
    SUCCESS_ALERT = (By.CLASS_NAME, 'alert-success')
    SUCCESS_MESSAGE = 'Success: You have added'

    def load(self):
        self.navigate_to_url(self.CATALOG_PAGE_URL)

    def is_display_control_displayed(self):
        return self.is_element_displayed(*self.DISPLAY_CONTROL)

    def is_product_list_displayed(self):
        return self.is_element_displayed(*self.PRODUCT_LIST)

    def is_product_thumb_displayed(self):
        return self.is_element_displayed(*self.PRODUCT_THUMB)

    def is_description_displayed(self):
        return self.is_element_displayed(*self.DESCRIPTION)

    def is_price_displayed(self):
        return self.is_element_displayed(*self.PRICE)

    def click_add_button(self, product_name):
        product = self.find_element(By.PARTIAL_LINK_TEXT, product_name)
        add_to_cart_button = product.find_element(*self.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def is_success_message_displayed(self):
        return self.is_element_displayed(*self.SUCCESS_ALERT)

    def is_product_in_list(self, product_name):
        products = self.find_elements(By.PARTIAL_LINK_TEXT, product_name)
        return len(products) > 0
