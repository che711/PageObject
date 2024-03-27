import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es', help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    chromedriver_path = './chromedriver'
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument("user-agent='Mozilla/5.0 ("
                         "Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 ("
                         "KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'")

    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    browser.maximize_window()
    time.sleep(2)
    yield browser
    time.sleep(2)
    browser.quit()
