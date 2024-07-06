import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

baseUrl = 'https://www.qa-practice.com/'

@pytest.fixture(scope="session")
def browser():

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()