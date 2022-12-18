from selenium.webdriver.common.by import By

from automation_lessons.my_framework.utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __title = 'Вікіпедія'
    __search = (By.CSS_SELECTOR, '.vector-search-box-inner')
    __login_button = (By.XPATH, '//li[@id="pt-login"]')
    __not_logged_in = (By.XPATH, '//li[@id="pt-anonuserpage"]//span')
    __topics = (By.XPATH, '//div[@id="topics"]')

    def is_title(self):
        return self.check_title(self.__title)

    def search_is_visible(self):
        return self._is_visible(self.__search)

    def login_button_is_clickable(self):
        return self._is_clickable(self.__login_button)

    def not_logged_in_is_visible(self):
        return self._is_visible(self.__not_logged_in)

    def topics_is_visible(self):
        return self._is_visible(self.__topics)
