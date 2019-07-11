from selenium import webdriver
import math 

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/execute_script.html')
x = browser.find_element_by_id('input_value')
x = math.log(abs(12 * math.sin(int(x.text))))

#browser.execute_script("window.scrollBy(0, 100);")
#browser.execute_script('window.scrollBy(0, 100);')
answer = browser.find_element_by_id('answer')
answer.send_keys(str(x))
robotCheckbox = browser.find_element_by_id('robotCheckbox')
robotCheckbox.click()
btn = browser.find_element_by_css_selector('button.btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

robotsRule = browser.find_element_by_id('robotsRule')
robotsRule.click()
btn.click()


