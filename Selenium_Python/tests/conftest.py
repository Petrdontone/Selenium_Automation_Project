import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options

"""
Класс Options в Selenium обычно используется в сочетании с желаемыми возможностями кастомизации Selenium WebDriver. 
Так вы можете выполнять различные операции, такие как открытие браузера (Chrome, Firefox, Safari, IE, Edge и т. д.)
"""


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, executable_path="/Users/yasnetsovpetr/Downloads/chromedriver 3")
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://demoqa.com/'
    driver.get(url)
    yield driver
    driver.quit()
