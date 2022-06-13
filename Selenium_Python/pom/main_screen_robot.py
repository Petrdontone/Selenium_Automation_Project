from selenium.webdriver.common.by import By
from Selenium_Python.base.seleniumbase import BasePage


class MainScreenLocators:
    LOCATOR_WIDGET_ELEMENTS = (By.CSS_SELECTOR, '.card svg:first-child')


class MainScreenHelpers(BasePage):

    def click_elements_widget(self):
        return self.find_element(MainScreenLocators.LOCATOR_WIDGET_ELEMENTS).click()
