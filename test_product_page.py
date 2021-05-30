from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
from selenium import webdriver
from .pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
import math


def test_push_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    time.sleep(2)
    basket = browser.find_element(*ProductPageLocators.BUTTON_BASKET)
    basket.click()
    print("\nНажата кнопка 'Add to basket'")

    promt = BasePage(browser, link)
    promt.solve_quiz_and_get_code()
    time.sleep(3)
    browser.quit()


