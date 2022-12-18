from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 20)

    def __wait_until_element_located(self, locator):
        return self.__wait.until(ES.presence_of_element_located(locator))

    def __wait_until_element_clickable(self, locator):
        return self.__wait.until(ES.element_to_be_clickable(locator))

    def __wait_until_element_visible(self, locator):
        return self.__wait.until(ES.visibility_of_element_located(locator))

    def __text_to_be_present(self, locator, text):
        return self.__wait.until(ES.text_to_be_present_in_element(locator, text))

    def __wait_until_element_to_be_selected(self, locator):
        return self.__wait.until(ES.element_to_be_selected(locator))

    def _send_keys(self, locator, value):
        element = self.__wait_until_element_located(locator)
        element.clear()
        element.send_keys(value)

    def _is_visible(self, locator):
        try:
            self.__wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _is_clickable(self, locator):
        try:
            self.__wait_until_element_clickable(locator)
            return True
        except TimeoutException:
            return False

    def _click(self, locator):
        element = self.__wait_until_element_clickable(locator)
        element.click()

    def check_title(self, title):
        if self._driver.title == title:
            return True
        return False

    def check_text_in_page(self, locator, text):
        try:
            self.__text_to_be_present(locator, text)
            return True
        except TimeoutException:
            return False

