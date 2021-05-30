from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
from selenium import webdriver
from .pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
import math


def test_push_add_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    # browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(2)
    basket = browser.find_element(*ProductPageLocators.BUTTON_BASKET)
    basket.click()
    promt = BasePage(browser, url)
    promt.solve_quiz_and_get_code()
    time.sleep(3)
    browser.quit()


