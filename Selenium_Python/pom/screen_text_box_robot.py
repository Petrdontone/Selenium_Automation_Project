from selenium.webdriver.common.by import By
from Selenium_Python.base.seleniumbase import BasePage


class ScreenTextBoxLocators:
    LOCATOR_FULL_NAME_CHECK = (By.CSS_SELECTOR, '#userName-label')
    LOCATOR_EMAIL_CHECK = (By.CSS_SELECTOR, '#userEmail-label')
    LOCATOR_CURRENT_ADDRESS_CHECK = (By.CSS_SELECTOR, '#currentAddress-label')
    LOCATOR_PERMANENT_ADDRESS_CHECK = (By.CSS_SELECTOR, '#permanentAddress-label')
    LOCATOR_SUBMIT_BUTTON_CHECK = (By.CSS_SELECTOR, '#submit')
    LOCATOR_CHECK_WINDOW_AFTER_CLICK_SUBMIT = (By.CSS_SELECTOR, '[class="border col-md-12 col-sm-12"]')

    LOCATOR_FULL_NAME_SEND_KEYS = (By.CSS_SELECTOR, '#userName')
    LOCATOR_EMAIL_CHECK_SEND_KEYS = (By.CSS_SELECTOR, '#userEmail')
    LOCATOR_CURRENT_ADDRESS_SEND_KEYS = (By.CSS_SELECTOR, '#currentAddress')
    LOCATOR_PERMANENT_ADDRESS_SEND_KEYS = (By.CSS_SELECTOR, '#permanentAddress')


class ScreenTextBoxHelpers(BasePage):
    def check_all_elements_screen(self):
        element_full_name = self.visible_element(ScreenTextBoxLocators.LOCATOR_FULL_NAME_CHECK).is_displayed()
        element_email = self.visible_element(ScreenTextBoxLocators.LOCATOR_EMAIL_CHECK).is_displayed()
        element_current_address = self.visible_element(
            ScreenTextBoxLocators.LOCATOR_CURRENT_ADDRESS_CHECK).is_displayed()
        element_permanent_address = self.visible_element(
            ScreenTextBoxLocators.LOCATOR_PERMANENT_ADDRESS_CHECK).is_displayed()
        element_submit_button = self.visible_element(ScreenTextBoxLocators.LOCATOR_SUBMIT_BUTTON_CHECK).is_displayed()
        return [element_full_name, element_email, element_current_address, element_permanent_address,
                element_submit_button]

    def send_keys_all_elements(self):
        element_full_name = self.visible_element(ScreenTextBoxLocators.LOCATOR_FULL_NAME_SEND_KEYS).send_keys("Peter")
        element_email = self.visible_element(ScreenTextBoxLocators.LOCATOR_EMAIL_CHECK_SEND_KEYS).send_keys(
            "name@mail.ru")
        element_current_address = self.visible_element(
            ScreenTextBoxLocators.LOCATOR_CURRENT_ADDRESS_SEND_KEYS).send_keys("Address test")
        element_permanent_address = self.visible_element(
            ScreenTextBoxLocators.LOCATOR_PERMANENT_ADDRESS_SEND_KEYS).send_keys("Permanent test address")
        return [element_full_name, element_email, element_current_address, element_permanent_address]

    def click_button(self):
        return self.find_element(ScreenTextBoxLocators.LOCATOR_SUBMIT_BUTTON_CHECK).click()

    def check_new_window(self):
        return self.visible_element(ScreenTextBoxLocators.LOCATOR_CHECK_WINDOW_AFTER_CLICK_SUBMIT).is_displayed()