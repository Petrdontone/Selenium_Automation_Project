import time

from allure_commons.types import Severity

from Selenium_Python.pom.main_screen_robot import MainScreenHelpers
from Selenium_Python.pom.screen_elements_robot import ScreenElementsHelpers
from Selenium_Python.pom.screen_text_box_robot import ScreenTextBoxHelpers
import allure


@allure.title('Проверка отправки формы текст бокса')
@allure.severity(Severity.NORMAL)
def test_submit_form_to_text_box(setup):
    with allure.step('1. Создаем инстанс хелпер класса'):
        main_page = MainScreenHelpers(setup)
    with allure.step('2. Нажимаем на виджет Elements'):
        main_page.click_elements_widget()
    with allure.step('3. Создаем инстанс хелпер класса'):
        screen_elements = ScreenElementsHelpers(setup)
    with allure.step('4. Нажимаем на элемент Text Box'):
        screen_elements.click_field_text_box()
    with allure.step('5. Создаем инстанс хелпер класса'):
        screen_text_box = ScreenTextBoxHelpers(setup)
    with allure.step('6. Проверяем все элементы, заполняем форму и нажимаем на кнопку Submit'):
        screen_text_box.check_all_elements_screen()
        screen_text_box.send_keys_all_elements()
        screen_text_box.click_button()
    with allure.step('7. Ожидаем появляющиеся окно с заполненными данными'):
        screen_text_box.check_new_window()
    time.sleep(3)
