from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_page import BasePage
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):
    BANNER = (By.ID, "carousel-banner-0")
    COMMON_HOME = (By.ID, "common-home")
    MENU = (By.ID, "menu")
    SECOND_BANNER = (By.ID, "carousel-banner-1")
    SEARCH = (By.ID, "search")
    MY_ACCOUNT_LINK = (By.XPATH, "//a[text()='My Account']")
    REGISTER_LINK = (By.CSS_SELECTOR, "#content > div > div:nth-child(1) > div > div > a")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency > div > a > span")
    CURRENCY_OPTIONS = (By.XPATH, '//a[@href="EUR"]')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price-new')

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.navigate_to_url("https://demo.opencart.com/")

    def is_banner_displayed(self):
        return self.is_element_displayed(*self.BANNER)

    def is_common_home_displayed(self):
        return self.is_element_displayed(*self.COMMON_HOME)

    def is_menu_displayed(self):
        return self.is_element_displayed(*self.MENU)

    def is_second_banner_displayed(self):
        return self.is_element_displayed(*self.SECOND_BANNER)

    def is_search_displayed(self):
        return self.is_element_displayed(*self.SEARCH)

    def click_my_account(self):
        my_account_link = self.find_element(*self.MY_ACCOUNT_LINK)
        self.driver.execute_script("arguments[0].click();", my_account_link)

    def click_register(self):
        self.click(*self.REGISTER_LINK)

    def is_logout_displayed(self):
        return self.is_element_displayed(By.LINK_TEXT, "Logout")

    def select_by_value(self, by_locator, value):
        dropdown = Select(self.find_element(*by_locator))
        dropdown.select_by_value(value)

    def show_currency_options(self):
        self.find_element(*self.CURRENCY_DROPDOWN).click()

    def select_currency(self, currency):
        euro_link = WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@href="EUR"]')))
        euro_link.click()

    def get_product_price(self):
        return self.find_element(*self.PRODUCT_PRICE).text
