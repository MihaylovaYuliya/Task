from selenium.webdriver.common.by import By
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")
    assert button, "button is not found"

	
