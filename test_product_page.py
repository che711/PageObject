from .pages.product_page import ProductPage
import time
from .pages.locators import ProductPageLocators




def test_add(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()

def test_name_book(browser):
    '''Return books name.'''
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.name_book()

def test_add_names_book(browser):
    '''Проверка имени книги, которую добавили в корзину'''
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    add_basket = browser.find_element(*ProductPageLocators.BUTTON_BASKET)
    add_basket.click()
    promt = ProductPage(browser, link)
    promt.solve_quiz_and_get_code()
    time.sleep(2)
    add_name2 = ProductPage(browser,link)
    add_name2.add_names_book()
    time.sleep(5)


def test_price_book(browser):
    '''Return books price'''
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.price_book()

def test_add_price_book(browser):
    '''Находим цену книги, добавленной в корзину'''
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.push_add_to_basket()
    time.sleep(2)
    page.add_price_book()


def test_guest_can_add_product_to_basket(browser):
    '''Проверка цены и книги в корзине'''
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    name1 = browser.find_element(*ProductPageLocators.NAME_BOOK)
    book1 = name1.text
    css_price1 = browser.find_element(*ProductPageLocators.PRICE_BOOK)
    price1 = css_price1.text
    page2 = ProductPage(browser, link)
    page2.open()
    add_basket = browser.find_element(*ProductPageLocators.BUTTON_BASKET)
    add_basket.click()
    promt = ProductPage(browser, link)
    promt.solve_quiz_and_get_code()
    time.sleep(2)
    promt = browser.find_element(*ProductPageLocators.ADD_NAME_BOOK)
    book2 = promt.text
    css_price2 = browser.find_element(*ProductPageLocators.ADD_PRICE_BOOK)
    price2 = css_price2.text
    print(f"\n\tСтоимость корзины: {price2}")
    print(f"\tДобавлена книга: {book2}")
    assert (price1 == price2), "Цены разные"
    assert (book1 == book2), "Книги разные"
