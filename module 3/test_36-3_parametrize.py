import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link',[
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
])

class TestFindAliens(object):
    alien_text = ''
    def test_find_alien_on_page(self, browser, link):
        browser.get(link)
        text = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea.ember-auto-resize.ember-view")))
        answer = str(math.log(int(time.time())))
        text.send_keys(answer)
        btn =  WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        btn.click()
        result = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        result = result.text
        assert result == 'Correct!', result