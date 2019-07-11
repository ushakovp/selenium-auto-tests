from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

a = browser.find_element_by_id('num1')
b = browser.find_element_by_id('num2')
sum = int(a.text) + int(b.text)

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(sum))

time.sleep(2)
btn = browser.find_element_by_css_selector('button.btn')
btn.click()