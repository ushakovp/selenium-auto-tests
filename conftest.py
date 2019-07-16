import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()