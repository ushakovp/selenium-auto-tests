from selenium import webdriver
import math
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

btn = browser.find_element_by_css_selector('button.trollface')
btn.click()

new_window = browser.window_handles[1]
browser.switch_to_window(new_window)

x = browser.find_element_by_id('input_value')
x = math.log(abs(12 * math.sin(int(x.text))))
answer = browser.find_element_by_id('answer')
answer.send_keys(str(x))
btn = browser.find_element_by_css_selector('button.btn')
btn.click()