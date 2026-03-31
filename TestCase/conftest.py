

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser").lower().strip()
    print("Browser value is:", browser)
    if browser :
        browser = browser.lower().strip()

    if browser == "chrome":
        print("Lunching chrome browser")
        # from selenium import webdriver
        driver = webdriver.Chrome()


    elif browser == "firefox":
        print("Lunching firefox browser")
        # from selenium import webdriver
        driver = webdriver.Firefox()

    elif browser == "edge":
        print("lunching edge browser")
        # from selenium import webdriver
        driver = webdriver.Edge()

    # elif browser == "headless":
    #      print("lunching headless browser")
    #      from selenium import webdriver
    #      from selenium.webdriver.chrome.options import Options
    #      chrome_options = Options()
    #      chrome_options.add_argument("--headless")
    #      driver = webdriver.Chrome(options = chrome_options)
    else:
        raise Exception(f"Invalid Browser: {browser}")
        # print("Invalid browser")
        # driver = None


    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
