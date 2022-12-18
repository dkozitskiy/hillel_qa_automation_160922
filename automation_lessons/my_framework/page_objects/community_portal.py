from selenium.webdriver.common.by import By
from automation_lessons.my_framework.utilities.web_ui.base_page import BasePage


class CommunityPortal(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __title = 'Вікіпедія:Портал спільноти — Вікіпедія'
    __menu_container = (By.XPATH, '//div[@id="menu-container"]')
    __lock = (By.XPATH, '//div[@id="menu-container"]')
    __how_to_help = (By.XPATH, '//td[@rowspan="3"]')
    __assist_and_social_life = (By.XPATH, '//td[@colspan="2"] //h2[@class="ext-discussiontools-init-section"]/..')
    __page_url = 'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8'

    def is_title(self):
        return self.check_title(self.__title)

    def menu_container_is_visible(self):
        return self._is_visible(self.__menu_container)

    def lock_is_visible(self):
        return self._is_visible(self.__lock)


    def how_to_help_is_visible(self):
        return self._is_visible(self.__how_to_help)

    def assist_and_social_life_is_visible(self):
        return self._is_visible(self.__assist_and_social_life)

    def check_url(self):
        return self.is_url_to_be(self.__page_url)
