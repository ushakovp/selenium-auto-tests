from selenium import webdriver
import math
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
accept = browser.find_element_by_css_selector('button.btn')
accept.click()
confirm = browser.switch_to_alert()
confirm.accept()

x = browser.find_element_by_id('input_value')
x = math.log(abs(12 * math.sin(int(x.text))))
answer = browser.find_element_by_id('answer')
answer.send_keys(str(x))
btn = browser.find_element_by_css_selector('button.btn')
btn.click()