from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '10000')
)
btn = browser.find_element_by_id('book')
btn.click()

x = browser.find_element_by_id('input_value')
x = math.log(abs(12 * math.sin(int(x.text))))
answer = browser.find_element_by_id('answer')
answer.send_keys(str(x))
btn = browser.find_element_by_id('solve')
btn.click()