from selenium.webdriver.common.by import By

from automation_lessons.less2.utilities.web_ui.base_page import BasePage


class PythonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __user_locator = (By.XPATH, '//li[@id="pt-userpage"]//span')

    def is_login_visible(self):
        return self._is_visible(self.__user_locator)

    def is_clickable_name(self):
        return self._is_clickable(self.__user_locator)
