from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.CURRENT_URL), "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True


"""
Структура:
 LoginPage:
   в should_be_login_url проверяем в assert не равена ли строка self.url через find строке login.  (!= -1)
   в shold_be_login_form и register_form ищем через id login_form или register_form в locators
   
  В шаблоне login_page.py запуск всех проверок собран в одном методе should_be_login_page(self). 
  При организации "красных" тестов его нужно запускать как минимум 3 раза (по кличеству функций в методе), поскольку 
  падение любой из них останавливает дальнейшее выполнение. Дополнительно у меня проверка форм авторизации и регистрации 
  выполнена по наличию на этих формах всех необходимых полей: емейл, пароль, ссылка если забыл пароль, кнопка accept 
  и т.д. - в сумме 8 элементов. Т.е. в моем случае "красные" тесты это 9 запусков (8 от форм + 1 от проверки 
  наличия 'login' в ссылке).

Можно как-то организовать это "более лучше" за один запуск, чтобы проверка сразу писала: нет такой кнопки, отсутствует 
такое поле, ссылка не верная? Сейчас у меня, например, функция should_be_login_form(self) - это 4 последовательных 
assert'а: 2 поля, 1 кнопка и 1 ссылка "забыл пароль". Падает на первом ошибочном элементе, последующие не проверяются.

Дополнительно создал тестовый класс test_login_page.py, вынес в него три новых теста. С проверкой URL пришлось немного 
поломать голову - тут нужно просто учесть, что мы ищем строку в строке.
 
Я для url использовал функцию open из родительского класса, не зря же мы ее писали.
assert "/login" in self.open(), "login is absent in current url"
 
а ведь можно тут дополнительно использовать регулярные выражения к проверке url с поиском по окончанию строки
И еще вынести ожидаемый результат в константу в LoginPageLocators, то есть /login/ .
Мысль если выполнить через in , то не факт что мы находимся именно на странице login, а не с её содержанием, 
hапример login/auth/.Но если будет баг и вдруг ссылка окажется login/login, то тут надо допиливать :))

self.url и self.browser.current_url??

"""