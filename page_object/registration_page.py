import time

from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class RegistrationPage(BasePage):
    ROW = (By.CLASS_NAME, "row")
    FORM_REGISTER = (By.ID, "form-register")
    ACCOUNT = (By.ID, "account")
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    PASSWORD_INPUT = (By.ID, 'input-password')
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, '#form-register > div > div > div > input')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#form-register > div > div > button")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        self.navigate_to_url("https://demo.opencart.com/index.php?route=account/register")

    def is_row_displayed(self):
        return self.is_element_displayed(*self.ROW)

    def is_form_register_displayed(self):
        return self.is_element_displayed(*self.FORM_REGISTER)

    def is_account_displayed(self):
        return self.is_element_displayed(*self.ACCOUNT)

    def is_first_name_input_displayed(self):
        return self.is_element_displayed(*self.FIRST_NAME_INPUT)

    def is_last_name_input_displayed(self):
        return self.is_element_displayed(*self.LAST_NAME_INPUT)

    def is_email_input_displayed(self):
        return self.is_element_displayed(*self.EMAIL_INPUT)

    def is_password_input_displayed(self):
        return self.is_element_displayed(*self.PASSWORD_INPUT)

    def is_privacy_policy_checkbox_displayed(self):
        return self.is_element_displayed(*self.PRIVACY_POLICY_CHECKBOX)

    def is_continue_button_displayed(self):
        return self.is_element_displayed(*self.CONTINUE_BUTTON)

    def fill_in_registration_form(self, first_name, last_name, email, password):
        self.fill_in_field(self.FIRST_NAME_INPUT, first_name)
        self.fill_in_field(self.LAST_NAME_INPUT, last_name)
        self.fill_in_field(self.EMAIL_INPUT, email)
        self.fill_in_field(self.PASSWORD_INPUT, password)

    def agree_to_terms(self):
        self.click(*self.PRIVACY_POLICY_CHECKBOX)

    def submit_registration_form(self):
        time.sleep(2)
        self.click(*self.CONTINUE_BUTTON)

    def is_success_alert_displayed(self):
        return self.is_element_displayed(*self.SUCCESS_ALERT)

    def is_logout_displayed(self):
        return self.is_element_displayed(*self.LOGOUT_BUTTON)
