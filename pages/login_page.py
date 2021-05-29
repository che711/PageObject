from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self,):
        assert (self.url in self.browser.current_url), "Login is not found in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"


"""
1. В файле locators.py создайте класс LoginPageLocators 
2. Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators
3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное 
сообщение об ошибке. Напишите сначала красный тест, чтобы убедиться в понятности вывода. 
4. В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем 
url браузера. Для этого используйте соответствующее свойство Webdriver.

5. Добавьте изменения в коммит с осмысленным сообщением
def should_be_login_url (full_string, substring):
	assert (substring in full_string), f"expected '{substring}' to be substring of '{full_string}'"

Структура:
LoginPage:
   в should_be_login_url проверяем в assert не равена ли строка self.url через find строке login.  (!= -1)
   в shold_be_login_form и register_form ищем через id login_form или register_form в locators
   
В шаблоне login_page.py запуск всех проверок собран в одном методе should_be_login_page(self). 
При организации "красных" тестов его нужно запускать как минимум 3 раза (по кличеству функций в методе), 
поскольку падение любой из них останавливает дальнейшее выполнение. Дополнительно у меня проверка 
форм авторизации ирегистрации выполнена по наличию на этих формах всех необходимых полей: емейл, пароль, 
сылка если забыл пароль, кнопка accept b т.д. - в сумме 8 элементов. 
Т.е. в моем случае "красные" тесты это 9 запусков (8 от форм + 1 от проверки наличия 'login' в ссылке).

В голове каша полнейшая. Мы пишем в файле Locators новый класс и в нем локаторы для формы регистрации и логина. 
В файле логин_пейдж пишем проверки с ассертами, а так же туда делаем импорт класса LoginPageLocators из 
локаторс. А потом в файле test_main_page пишем сами проверки которые запускаются пайтестом?

Можно как-то организовать это "более лучше" за один запуск, чтобы проверка сразу писала: нет такой кнопки, 
отсутствует такое поле, ссылка не верная? Сейчас у меня, например, функция should_be_login_form(self) - 
это 4 последовательных assert'а: 2 поля, 1 кнопка и 1 ссылка "забыл пароль". Падает на первом ошибочном 
элементе, последующие не проверяются.

Дополнительно создал тестовый класс test_login_page.py, вынес в него три новых теста. С проверкой URL 
пришлось немного поломать голову - тут нужно просто учесть, что мы ищем строку в строке.
 
Я для url использовал функцию open из родительского класса, не зря же мы ее писали.
assert "/login" in self.open(), "login is absent in current url"
 
а ведь можно тут дополнительно использовать регулярные выражения к проверке url с поиском по окончанию строки
И еще вынести ожидаемый результат в константу в LoginPageLocators, то есть /login/ .
Мысль если выполнить через in , то не факт что мы находимся именно на странице login, а не с её содержанием, 
hапример login/auth/.Но если будет баг и вдруг ссылка окажется login/login, то тут надо допиливать :))

self.url и self.browser.current_url??

"""