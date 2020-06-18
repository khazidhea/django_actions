import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_basic(live_server):
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        driver = webdriver.Remote(command_executor='http://192.168.96.1:9515')

    driver.get(live_server.url)
    counter = driver.find_element_by_id('counter')
    assert '1' == counter.text

    driver.refresh()
    counter = driver.find_element_by_id('counter')
    assert '2' == counter.text

    driver.close()
