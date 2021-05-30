from .pages.product_page import ProductPage
import time


# def test_guest_can_add_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
#     page = ProductPage(browser, link)
#     page.open()


def test_push_add_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, url)
    page.open()
    page.push_add_to_basket
    time.sleep(2)


# def test_go_to_confirm(browser):
#     pass





