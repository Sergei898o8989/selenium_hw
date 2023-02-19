import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome, firefox, or edge")
    parser.addoption("--url", action="store", default="https://demo.opencart.com",
                     help="Specify the base URL of the Opencart demo site")


@pytest.fixture(scope="module")
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    # Get the path to the web driver executable
    driver_path = os.path.join(os.getcwd(), "C:\\Users\\1\\Downloads\\Drivers")

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=os.path.join(driver_path, "chromedriver.exe"))
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path=os.path.join(driver_path, "msedgedriver.exe"))
    else:
        raise ValueError("Invalid browser choice. Choose from chrome, firefox, or edge.")

    driver.get(url)

    yield driver
    driver.quit()
