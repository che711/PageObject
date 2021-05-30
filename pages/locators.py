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
