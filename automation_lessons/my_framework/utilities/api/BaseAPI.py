import json
import requests


class BaseAPI:
    def __init__(self):
        self.__request = requests

    def get(self, base_url, url):
        response = self.__request.get(f'{base_url}{url}')
        return response












    def post(self, url, body={'gender': 'female'}):
        json_obj = json.dumps(body)
        response = self.__request(url, json=json_obj)
        return response

