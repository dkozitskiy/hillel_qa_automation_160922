import pytest


@pytest.mark.regression
def test_title_name(open_reset_password_page):
    assert open_reset_password_page.title() is True


@pytest.mark.regression
def test_left_menu_in_login_page(open_reset_password_page):
    assert open_reset_password_page.left_menu_is_visible() is True


@pytest.mark.regression
def test_name_input_in_page(open_reset_password_page):
    assert open_reset_password_page.name_input_is_visible() is True


@pytest.mark.regression
def test_email_input_in_page(open_reset_password_page):
    assert open_reset_password_page.email_address_input_is_visible() is True

@pytest.mark.regression
def test_reset_password_button_is_clickable(open_reset_password_page):
    assert open_reset_password_page.reset_password_button_is_clickable() is True