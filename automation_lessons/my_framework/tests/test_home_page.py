import pytest


@pytest.mark.regression
def test_title_name(open_home_page):
    assert open_home_page.is_title() is True


@pytest.mark.regression
def test_search_in_page(open_home_page):
    assert open_home_page.search_is_visible() is True


@pytest.mark.regression
def test_login_button(open_home_page):
    assert open_home_page.login_button_is_clickable() is True


@pytest.mark.regression
def test_not_logged_in_title(open_home_page):
    assert open_home_page.not_logged_in_is_visible() is True
