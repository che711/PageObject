from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")




class LoginPageLocators():
    CURRENT_URL = (By.CSS_SELECTOR, "current_url")
    ADDRES_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
