from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        """
        self - это такой маячок-указатель для переменных и функций внутри класса
        Первым делом добавим конструктор — 
        метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__.
        """

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def visible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator),
                                                      message=f"Can't visibility your element {locator}")
