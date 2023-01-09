from automation_lessons.data.gender import Gender
from automation_lessons.my_framework.utilities.api.BaseAPI import BaseAPI


class NameAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '?name='

    def get_gender_by_name(self, base_url, name):
        return self.get(base_url, f'{self.__url}{name}')

    def create_gender(self, base_url, body=None):
        gender_data = Gender()
        if body is not None:
            gender_data = gender_data
        else:
            gender_data.update_dict(**body)
        response = self.post(base_url, body=gender_data.get_json())
        return response
