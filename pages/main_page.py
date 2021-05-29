from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators



class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

