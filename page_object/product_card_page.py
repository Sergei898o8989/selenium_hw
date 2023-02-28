from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductCardPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    COL_SM = (By.CLASS_NAME, "col-sm")
    DESCRIPTION = (By.ID, "tab-description")
    FORM_PRODUCT = (By.ID, "form-product")
    PRODUCT = (By.ID, "product")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demo.opencart.com/index.php?route=product/product&product_id=42"

    def load(self):
        self.navigate_to_url(self.url)

    def is_add_to_cart_button_displayed(self):
        return self.is_element_displayed(*self.ADD_TO_CART_BUTTON)

    def is_col_sm_displayed(self):
        return self.is_element_displayed(*self.COL_SM)

    def is_description_displayed(self):
        return self.is_element_displayed(*self.DESCRIPTION)

    def is_form_product_displayed(self):
        return self.is_element_displayed(*self.FORM_PRODUCT)

    def is_product_displayed(self):
        return self.is_element_displayed(*self.PRODUCT)
