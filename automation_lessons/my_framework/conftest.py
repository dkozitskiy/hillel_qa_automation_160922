import pytest

from automation_lessons.my_framework.page_objects.login_page import LoginPage
from automation_lessons.my_framework.page_objects.reset_password_page import ResetPasswordPage
from automation_lessons.my_framework.utilities.config_parser import ReadConfig
from automation_lessons.my_framework.utilities.driver_factory import DriverFactory


# @pytest.fixture()
# def create_driver():
#     driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
#     driver.maximize_window()
#     driver.get(ReadConfig.get_base_url())
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture()
# def open_login_page(create_driver):
#     return LoginPage(create_driver)


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    create_driver.get(ReadConfig.get_base_url())
    return LoginPage(create_driver)


@pytest.fixture()
def open_reset_password_page(create_driver):
    create_driver.get(ReadConfig.reset_password_page_url())
    return ResetPasswordPage(create_driver)


@pytest.fixture()
def open_home_page(create_driver):
    create_driver.get(ReadConfig.get_home_page())
    return ResetPasswordPage(create_driver)
