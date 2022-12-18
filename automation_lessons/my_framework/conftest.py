import pytest

from automation_lessons.my_framework.page_objects.community_portal import CommunityPortal
from automation_lessons.my_framework.page_objects.home_page import HomePage
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
    create_driver.get('https://uk.wikipedia.org/wiki/')
    return HomePage(create_driver)


@pytest.fixture()
def open_community_portal(create_driver):
    create_driver.get('https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8')
    return CommunityPortal(create_driver)
