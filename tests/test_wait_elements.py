from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_home_page(browser):
    browser.get("https://demo.opencart.com/")
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    assert browser.find_element(By.ID, "carousel-banner-0").is_displayed()
    assert browser.find_element(By.ID, "common-home").is_displayed()
    assert browser.find_element(By.ID, "menu").is_displayed()
    assert browser.find_element(By.ID, "carousel-banner-1").is_displayed()
    assert browser.find_element(By.ID, "search").is_displayed()


def test_catalog_page(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/category&path=20")
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    assert browser.find_element(By.ID, "display-control").is_displayed()
    assert browser.find_element(By.ID, "product-list").is_displayed()
    assert browser.find_element(By.CLASS_NAME, "product-thumb").is_displayed()
    assert browser.find_element(By.CLASS_NAME, "description").is_displayed()
    assert browser.find_element(By.CLASS_NAME, "price").is_displayed()


def test_product_card_page(browser):
    browser.get("https://demo.opencart.com/index.php?route=product/product&product_id=42")
    WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    assert browser.find_element(By.ID, "product").is_displayed()
    assert browser.find_element(By.ID, "form-product").is_displayed()
    assert browser.find_element(By.CLASS_NAME, "col-sm").is_displayed()
    assert browser.find_element(By.ID, "product").is_displayed()
    assert browser.find_element(By.ID, "form-product").is_displayed()


def test_admin_login_page(browser):
    browser.get("https://demo.opencart.com/admin/")
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    assert browser.find_element(By.CLASS_NAME, "card-header").is_displayed()
    assert browser.find_element(By.CLASS_NAME, "card-body").is_displayed()
    assert browser.find_element(By.ID, "form-login").is_displayed()
    assert browser.find_element(By.LINK_TEXT, "Forgotten Password").is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, "button[type='submit'].btn-primary").is_displayed()


def test_user_registration_page(browser):
    browser.get("https://demo.opencart.com/index.php?route=account/register")
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "account-register"))
    )
    assert browser.find_element(By.CLASS_NAME, "row").is_displayed()
    assert browser.find_element(By.ID, "form-register").is_displayed()
    assert browser.find_element(By.ID, "account").is_displayed()
    assert browser.find_element(By.NAME, "agree").is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']").is_displayed()
