import pytest


@pytest.mark.regression
def test_title_name(open_community_portal):
    assert open_community_portal.is_title() is True


@pytest.mark.regression
def test_menu_container_in_page(open_community_portal):
    assert open_community_portal.menu_container_is_visible() is True


@pytest.mark.regression
def test_lock_in_page(open_community_portal):
    assert open_community_portal.lock_is_visible() is True


@pytest.mark.regression
def test_how_to_help_in_page(open_community_portal):
    assert open_community_portal.how_to_help_is_visible() is True


@pytest.mark.regression
def test_assist_and_social_lifein_page(open_community_portal):
    assert open_community_portal.assist_and_social_life_is_visible() is True


@pytest.mark.regression
def test_page_url(open_community_portal):
    assert open_community_portal.check_url() is True