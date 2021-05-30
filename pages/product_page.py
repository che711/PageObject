from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def push_add_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        add_basket.click()
        promt = BasePage(self.browser, self.url)
        promt.solve_quiz_and_get_code()


    def name_book(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        book = name.text
        print(f"\n\tКнига называется: {book}")

    def add_names_book(self):
        name2 = self.browser.find_element(*ProductPageLocators.ADD_NAME_BOOK)
        book = name2.text
        print(f"\n\tКнига называется: {book}")





