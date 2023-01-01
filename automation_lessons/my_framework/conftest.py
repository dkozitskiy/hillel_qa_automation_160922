import json
import pytest

from automation_lessons.my_framework.CONSTANTS import ROOT_DIR
from automation_lessons.my_framework.page_objects.community_portal import CommunityPortal
from automation_lessons.my_framework.page_objects.home_page import HomePage
from automation_lessons.my_framework.page_objects.login_page import LoginPage
from automation_lessons.my_framework.page_objects.reset_password_page import ResetPasswordPage
from automation_lessons.my_framework.utilities.config_parser import ReadConfig
from automation_lessons.my_framework.utilities.configuration import Configuration
from automation_lessons.my_framework.utilities.driver_factory import DriverFactory


@pytest.fixture(scope="session")
def env():
    with open(f'{ROOT_DIR}/configurations/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)

    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(ReadConfig.get_browser_id())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver, env):
    create_driver.get(env.base_url)
    return LoginPage(create_driver)


@pytest.fixture()
def open_reset_password_page(create_driver):
    create_driver.get(ReadConfig.reset_password_page_url())
    return ResetPasswordPage(create_driver)


@pytest.fixture()
def open_home_page(create_driver):
    create_driver.get(ReadConfig.get_start_page())
    return HomePage(create_driver)


@pytest.fixture()
def open_community_portal(create_driver):
    create_driver.get(ReadConfig.get_community_portal_page())
    return CommunityPortal(create_driver)
