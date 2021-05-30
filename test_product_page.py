from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
from selenium import webdriver
from .pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By



def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()
    time.sleep(10)

# def test_name_book(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = ProductPage(browser, link)
#     page.open()
#     page.name_book()

def test_add_name_book(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_names_book
    time.sleep(5)
