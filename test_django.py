from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_basic(live_server):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get(live_server.url)
    counter = driver.find_element_by_id('counter')
    assert '1' == counter.text

    driver.refresh()
    counter = driver.find_element_by_id('counter')
    assert '2' == counter.text

    driver.close()
