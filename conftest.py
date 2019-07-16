import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: Chrome or firefox")

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        print('Browser {} still is not implemented'.format(browser_name))
    yield browser
    browser.quit()