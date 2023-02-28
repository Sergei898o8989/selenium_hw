from faker import Faker

from page_object.admin_login_page import AdminLoginPage
from page_object.catalog_page import CatalogPage
from page_object.home_page import HomePage
from page_object.product_card_page import ProductCardPage
from page_object.registration_page import RegistrationPage


def test_home_page(browser):
    home_page = HomePage(browser)
    home_page.load()
    assert home_page.is_banner_displayed()
    assert home_page.is_common_home_displayed()
    assert home_page.is_menu_displayed()
    assert home_page.is_second_banner_displayed()
    assert home_page.is_search_displayed()


def test_catalog_page(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.load()
    assert catalog_page.is_display_control_displayed()
    assert catalog_page.is_product_list_displayed()
    assert catalog_page.is_product_thumb_displayed()
    assert catalog_page.is_description_displayed()
    assert catalog_page.is_price_displayed()


def test_product_card_page(browser):
    product_card_page = ProductCardPage(browser)
    product_card_page.load()
    assert product_card_page.is_product_displayed()
    assert product_card_page.is_form_product_displayed()
    assert product_card_page.is_col_sm_displayed()
    assert product_card_page.is_description_displayed()
    assert product_card_page.is_add_to_cart_button_displayed()


def test_admin_login_page(browser):
    admin_login_page = AdminLoginPage(browser)
    admin_login_page.load()
    assert admin_login_page.is_card_header_displayed()
    assert admin_login_page.is_card_body_displayed()
    assert admin_login_page.is_form_login_displayed()
    assert admin_login_page.is_forgotten_password_link_displayed()
    assert admin_login_page.is_login_button_displayed()


def test_user_registration_page(browser):
    registration_page = RegistrationPage(browser)
    registration_page.load()
    assert registration_page.is_row_displayed()
    assert registration_page.is_form_register_displayed()
    assert registration_page.is_account_displayed()


def test_register_user(browser):
    fake = Faker()
    email = fake.email()
    home_page = HomePage(browser)
    home_page.load()
    home_page.click_my_account()
    home_page.click_register()
    registration_page = RegistrationPage(browser)
    registration_page.fill_in_registration_form('Mister', 'Test', email, '123456!')
    registration_page.agree_to_terms()
    registration_page.submit_registration_form()
    # Check if user has been successfully registered and logged in
    assert home_page.is_logout_displayed()


def test_change_currency(browser):
    home_page = HomePage(browser)
    home_page.load()
    # Click on the currency dropdown to select Euro
    home_page.show_currency_options()
    home_page.select_currency("EUR")
    # Check that the product price is displayed in Euros
    assert "€" in home_page.get_product_price()
