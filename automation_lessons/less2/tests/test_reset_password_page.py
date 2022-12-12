import pytest


@pytest.mark.regression
def test_title_name(open_reset_password_page):
    assert open_reset_password_page.title() is True
