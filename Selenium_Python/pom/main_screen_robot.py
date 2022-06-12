from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage


class MainScreenLocators:
    LOCATORS_WIDGET_ELEMENTS = (By.CSS_SELECTOR, '.card svg:first-child')


class MainScreenHelpers(BasePage):

    def click_elements_widget(self):
        return self.find_element(MainScreenLocators.LOCATORS_WIDGET_ELEMENTS).click()
