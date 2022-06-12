import time

from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage


class ScreenElementsLocators:
    LOCATORS_MAIN_ELEMENTS = (By.CSS_SELECTOR, '.header-wrapper:nth-child(1)')
    LOCATORS_FILED_TEXT_BOX = (By.XPATH, '//span[text()="Text Box"]')


class ScreenElementsHelpers(BasePage):

    def click_field_element(self):
        return self.find_element(ScreenElementsLocators.LOCATORS_MAIN_ELEMENTS).click()

    def click_field_text_box(self):
        return self.find_element(ScreenElementsLocators.LOCATORS_FILED_TEXT_BOX).click()