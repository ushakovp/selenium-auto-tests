import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
    def test_registration_form1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        name = browser.find_element_by_css_selector(".first[required]")
        name.send_keys('Ivan')
        last_name = browser.find_element_by_css_selector(".second[required]")
        last_name.send_keys('Ivanov')
        email = browser.find_element_by_css_selector(".third[required]")
        email.send_keys('example@mail.com')

        btn = browser.find_element_by_css_selector('button.btn')
        btn.click()

        time.sleep(1)

        welcome_text = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text,'Registration failure')

    def test_registration_form2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

        name = browser.find_element_by_css_selector(".first[required]")
        name.send_keys('Ivan')
        last_name = browser.find_element_by_css_selector(".second[required]")
        last_name.send_keys('Ivanov')
        email = browser.find_element_by_css_selector(".third[required]")
        email.send_keys('example@mail.com')

        btn = browser.find_element_by_css_selector('button.btn')
        btn.click()

        time.sleep(1)

        welcome_text = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text,'Registration failure')

if __name__ == '__main__':
    unittest.main()