import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# pytest -s -v --browser_name=chrome test_parser.py
# pytest -s -v --browser_name=firefox test_parser.py



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(3)
    browser.quit()
