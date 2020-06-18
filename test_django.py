from selenium import webdriver


def test_basic(live_server):
    driver = webdriver.Firefox()

    driver.get(live_server.url)
    counter = driver.find_element_by_id('counter')
    assert '1' == counter.text

    driver.refresh()
    counter = driver.find_element_by_id('counter')
    assert '2' == counter.text

    driver.close()
