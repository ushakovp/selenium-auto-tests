from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

name = browser.find_element_by_name('firstname')
name.send_keys('Pa')
lastname = browser.find_element_by_name('lastname')
lastname.send_keys('Ush')
email = browser.find_element_by_name('email')
email.send_keys('mail@example.com')
send_file = browser.find_element_by_css_selector("[type='file']")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
send_file.send_keys(file_path)

btn = browser.find_element_by_css_selector('button.btn')
btn.click()