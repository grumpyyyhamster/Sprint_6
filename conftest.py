import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from data_to_use import TestData


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(options=options)
    driver.get(TestData.BASE_URL)
    yield driver
    driver.quit()
