"""
1. створіть наступну структуру
    - клас шкільний_персонал - абстрактний, клас ініт не має бути абстрактним, в ініті отримувати імя, прізвище, розмір зарплати. додайте
    абстрактний метод __str__
    - від нього наслідуються класи вчитель, технічний персонал - додайте якісь методи на свій розсуд. метод ініт тут не перевизначайте,
    ви його успадкуєте
    - клас школа - назва, директор, список вчителів, список технічного персоналу, проперті місячна зарплата
2. при створенні школи потрібно вказати, хто директор (екземпляр класу вчителів). також автоматично створити списки вчителів,
списки технічного персоналу (використайте ліст компрехеншн, імена та прізвища можна отримувати за допомогою рамдомного вибору із зовнішніх списків,
зарплата - рандомно від 10 000 до 50 000)
3. створити школу.
4. вивести список вчителів,
5. вивести місячну зп всього персоналу
6. додайте вчителя
7. змініть директора (школа без директора не може існувати, директор при цьому переходить в список вчителів, а вчитель стає директором,
і відповідно, видаляється зі списку вчителів)
"""
from abc import abstractmethod, ABC
from random import randint
from typing import Union

from faker import Faker

fake = Faker('ru_RU')


class SchoolStaff(ABC):

    def __init__(self, name: str, surname: str, salary: Union[int, float] = 10_000):
        self.name = name
        self.surname = surname
        self.salary = salary

    @abstractmethod
    def __str__(self):
        pass


class Teacher(SchoolStaff):
    """create a teacher"""

    def __str__(self):
        return f'Меня зовут {self.name} {self.surname}. Я буду Вас учить'


class TechnicalStaff(SchoolStaff):
    """create a technical officer"""

    def __str__(self):
        return f'Меня зовут {self.name} {self.surname}. Обращайтесь если что то сломалось'


class School:
    def __init__(self, title: str, director: Teacher, teachers_at_school: int = 1, technical_staff_at_school: int = 1):
        self.title = title
        self.director = director
        self.teachers_lst = [Teacher(fake.first_name(), fake.last_name(), randint(10000, 50000)) for employee in range(teachers_at_school)]
        self.technical_staff_lst = [Teacher(fake.first_name(), fake.last_name(), randint(10000, 50000)) for employee in
                                    range(technical_staff_at_school)]

    @property
    def get_total_salary_at_school(self):
        all_staff = []
        all_staff.append(self.director)
        all_staff += self.teachers_lst
        all_staff += self.technical_staff_lst
        total_salary = sum(object.salary for object in all_staff)
        return total_salary

    @property
    def get_technical_staff_lst(self):
        return self.technical_staff_lst

    @property
    def get_teachers_lst(self):
        return self.teachers_lst

    def add_teacher(self, ss):
        pass


school1 = School('Букварик', Teacher('Ирина', 'Гном', 20000))
print(School.get_total_salary_at_school)
t_list = school1.get_technical_staff_lst
print(t_list)

...
