"""
1. Напишіть декоратор, який перетворює результат роботи функції на стрінг
2. Напишіть докстрінг для цього декоратора
"""


def change_to_string(func):
    """
    This decorator that receives a function executes it. After that returns the result of the function as a string
    :param func: takes a function
    :return: returns the result of the received function as a string
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for arg in args:
            if not isinstance(arg, str):
                return str(result)
            else:
                return result
        for k, v in kwargs:
            if not isinstance(v, str):
                return str(result)
            else:
                return result

    return wrapper
