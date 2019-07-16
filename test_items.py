import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_link_on_the_product_page(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector(".btn-add-to-basket")