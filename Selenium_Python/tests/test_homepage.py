import time

from pom.main_screen_robot import MainScreenHelpers
from pom.screen_elements_robot import ScreenElementsHelpers


def test_go_widget(setup):
    main_page = MainScreenHelpers(setup)
    main_page.click_elements_widget()
    screen_elements = ScreenElementsHelpers(setup)
    screen_elements.click_field_element()
    screen_elements.click_field_text_box()
    time.sleep(5)