from selenium.webdriver.common.by import By

from automation_lessons.my_framework.utilities.web_ui.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __title = 'Скинути пароль — Вікіпедія'
    __left_menu = (By.XPATH, '//div[@id="mw-panel"]')
    __name_input = (By.XPATH, '//div//input[@name="wpUsername"]')

    def title(self):
        return self.check_title(self.__title)

    def left_menu_is_visible(self):
        return self._is_visible(self.__left_menu)

    def name_input_is_visible(self):
        return self._is_visible(self.__name_input)