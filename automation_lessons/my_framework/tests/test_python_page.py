import pytest
from automation_lessons.my_framework.utilities.config_parser import ReadConfig


@pytest.mark.regression
def test_clickable_name_in_login_page(open_login_page):
    login_page = open_login_page
    python_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert python_page.is_clickable_name() is True


@pytest.mark.regression
def test_title_name(open_login_page):
    login_page = open_login_page
    python_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert python_page.is_title() is True


@pytest.mark.regression
def test_left_menu_in_login_page(open_login_page):
    login_page = open_login_page
    python_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert python_page.is_content_menu_visible() is True


@pytest.mark.regression
def test_article_title(open_login_page):
    login_page = open_login_page
    python_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert python_page.is_article_title('Python') is True


@pytest.mark.regression
def is_test_page_url(open_login_page):
    login_page = open_login_page
    python_page = login_page.login(ReadConfig.get_login(), ReadConfig.get_password())
    assert python_page.is_check_url() is True
