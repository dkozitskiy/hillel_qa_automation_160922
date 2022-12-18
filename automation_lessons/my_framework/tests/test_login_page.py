import pytest

from automation_lessons.my_framework.utilities.config_parser import ReadConfig


@pytest.mark.regression
def test_title_name(open_login_page):
    assert open_login_page.title() is True


@pytest.mark.regression
@pytest.mark.parametrize('login, password', [('not_valid@test.net', ReadConfig.get_password()), (ReadConfig.get_login(), 'A1qwerty')])
def test_not_valid_login(open_login_page, login, password):
    open_login_page.login(login, password)
    assert open_login_page.check_not_valid_login_data() is True


@pytest.mark.regression
def test_left_menu_in_login_page(open_login_page):
    assert open_login_page.left_menu_is_visible() is True


@pytest.mark.regression
def test_header_in_login_page(open_login_page):
    assert open_login_page.header_is_visible() is True


@pytest.mark.smoke
def test_login(open_login_page):
    login_page = open_login_page
    python_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert python_page.is_login_visible() is True
