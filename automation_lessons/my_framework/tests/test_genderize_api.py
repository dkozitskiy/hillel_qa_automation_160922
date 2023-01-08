import requests
from http import HTTPStatus

from automation_lessons.api_collection.name_api import NameAPI


def test_get_genderize(env):
    response = NameAPI().get_gender_by_name(env.genderize_url, 'Igor')
    assert response.status_code == HTTPStatus.OK


def test_body_genderize(env):
    response = NameAPI().get_gender_by_name(env.genderize_url, 'Igor')
    s=1


