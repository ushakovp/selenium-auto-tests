from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/huge_form.html')
elements = browser.find_elements_by_css_selector("[type = 'text']")
print(elements)
for element in elements:
    element.send_keys('element')
button = browser.find_element_by_css_selector('button.btn')
button.click()
