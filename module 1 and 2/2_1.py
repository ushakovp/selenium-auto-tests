from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/math.html')

x = browser.find_element_by_id('input_value')
x = x.text
x = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(x)
robot_checkbox = browser.find_element_by_id('robotCheckbox')
robot_checkbox.click()
robot_radio = browser.find_element_by_id('robotsRule')
robot_radio.click()
btn = browser.find_element_by_css_selector('button.btn')
btn.click()
