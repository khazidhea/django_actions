import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.yield_fixture
def driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        driver = webdriver.Remote(command_executor='http://192.168.96.1:9515')
    driver.__enter__()
    yield driver
    driver.__exit__()
