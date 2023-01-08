from automation_lessons.my_framework.utilities.api.BaseAPI import BaseAPI


class NameAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '?name='

    def get_gender_by_name(self, base_url, name):
        return self.get(base_url, f'{self.__url}{name}')


