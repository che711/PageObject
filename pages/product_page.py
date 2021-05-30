from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def push_add_to_basket(self):
        add_basket = self.browser.find_element(By.CSS_SELECTOR, 'button.btn-lg:nth-child(3)')
        add_basket.click()
        time.sleep(3)




