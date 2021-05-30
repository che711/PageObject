from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    CURRENT_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_URL = 'http: // selenium1py.pythonanywhere.com / ru / accounts / login /'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    NAME_BOOK = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    ADD_NAME_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE_BOOK = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    ADD_PRICE_BOOK = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
