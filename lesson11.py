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
from random import randint, choice
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

    __repr__ = __str__


class TechnicalStaff(SchoolStaff):
    """create a technical officer"""

    def __str__(self):
        return f'Меня зовут {self.name} {self.surname}. Обращайтесь если что то сломалось'

    __repr__ = __str__


class School:
    """
    Creation of a new school. By default, the school creates 10 teachers and 3 technical staff. It is possible to set your own values for the state.
    For the name of the shakola, you must pass:
    title: (str)
    director: (Teacher)
    teachers_at_school: (int)
    technical_staff_at_school: (int)
    """

    def __init__(self, title: str, director: Teacher, teachers_at_school: int = 10, technical_staff_at_school: int = 3):
        self.title = title
        self.director = director
        self.teachers_lst = [Teacher(fake.first_name(), fake.last_name(), randint(10000, 50000)) for _ in range(teachers_at_school)]
        self.technical_staff_lst = [TechnicalStaff(fake.first_name(), fake.last_name(), randint(10000, 50000)) for _ in
                                    range(technical_staff_at_school)]

    @property
    def get_total_salary_at_school(self):
        """the method returns the total salary for the school"""
        all_staff = [self.director]
        all_staff += self.teachers_lst
        all_staff += self.technical_staff_lst
        total_salary = sum(object.salary for object in all_staff)
        return total_salary

    def change_director(self):
        """the method changes the director to a random teacher. principal becomes teacher"""
        old_director = self.director
        new_director = choice(self.teachers_lst)
        self.teachers_lst.append(old_director)
        self.director = new_director
        self.teachers_lst.remove(self.director)

    def get_teachers_lst(self):
        """to print the list of teachers"""
        return self.teachers_lst

    def technical_staff_lst(self):
        """to print the list of technical personnel"""
        return self.technical_staff_lst


if __name__ == '__main__':
    school1 = School('Букварик', Teacher('Ирина', 'Гном', 20000))
    school1.teachers_lst.append(Teacher('Игнат', 'Иванов', 11000))
    school1.change_director()
