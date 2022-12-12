from automation_lessons.less2.utilities.web_ui.base_page import BasePage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    __title = 'Скинути пароль — Вікіпедія'

    def title(self):
        return self.check_title(self.__title)