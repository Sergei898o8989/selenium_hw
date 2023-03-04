from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class AdminLoginPage(BasePage):
    # locators
    CARD_HEADER = (By.CLASS_NAME, "card-header")
    CARD_BODY = (By.CLASS_NAME, "card-body")
    FORM_LOGIN = (By.ID, "form-login")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#form-login > div.text-end > button")
    SECURITY_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '#modal-security > div > div > div.modal-header > button')
    USERNAME_FIELD = (By.ID, "input-username")
    PASSWORD_FIELD = (By.ID, "input-password")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demo.opencart.com/admin/"

    def load(self):
        self.navigate_to_url(self.url)

    def is_card_header_displayed(self):
        return self.is_element_displayed(*self.CARD_HEADER)

    def is_card_body_displayed(self):
        return self.is_element_displayed(*self.CARD_BODY)

    def is_form_login_displayed(self):
        return self.is_element_displayed(*self.FORM_LOGIN)

    def is_forgotten_password_link_displayed(self):
        return self.is_element_displayed(*self.FORGOTTEN_PASSWORD_LINK)

    def is_login_button_displayed(self):
        return self.is_element_displayed(*self.LOGIN_BUTTON)

    def login(self, username, password):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.find_element(*self.LOGIN_BUTTON).click()
