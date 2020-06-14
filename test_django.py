from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_basic():
    driver = webdriver.Remote(command_executor='http://192.168.96.1:9515')
    driver.get('http://127.0.0.1:8000/')
    assert 'Hello, world!' in driver.page_source
    driver.close()
