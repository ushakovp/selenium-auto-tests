from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

x = browser.find_element_by_id('treasure')
x = x.get_attribute('valuex')
x = calc(x)

answer = browser.find_element_by_id('answer')
answer.send_keys(x)
robotCheck = browser.find_element_by_id('robotCheckbox')
robotCheck.click()
robotRule = browser.find_element_by_id('robotsRule')
robotRule.click()
btn = browser.find_element_by_css_selector('button.btn')
btn.click()
