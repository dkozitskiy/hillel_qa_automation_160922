from selenium.webdriver.common.by import By
from automation_lessons.my_framework.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)