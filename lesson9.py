'''
1. напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)
2. напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає результатам роботи методу
capitalize() (перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)
3. написати до кожної функції мінімум 5 assert
4, написати декоратор, який добавляє принт з результатом роботи отриманої функції + текстовий параметр,
отриманий ним (декоратор з параметром - це там, де три функції)
при цьому очікувані результати роботи функції не змінюються (декоратор просто добавляє принт)
'''


# 4
def func_result_with_param(param=None):
    """
    this decorator adds the text information specified in the decorator parameter + the result of the function execution to the decorated function
    """

    def func_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(param, result)
            return result

        return wrapper

    return func_decorator


# 1
@func_result_with_param()
def pair_check(number: int) -> bool:
    """
    a function that checks whether the number passed to it is even or not (returns True or False).
    if not an int is passed to the function, the function will return False.
    :param number: takes an int to be checked for evenness
    :return: True or False depending on the number passed to the function
    """
    if type(number) is not int or number % 2 == 1:
        return False
    return True


# 2
@func_result_with_param()
def matching_capitalize(string: str) -> bool:
    """
    a function that accepts a string and determines whether this string corresponds to the results of the 'capitalize()' method
    if not an str is passed to the function, the function will return False.
    :param string: string to check
    :return: True or False depending on the string passed to the function
    """
    if type(string) is not str:
        return False
    if string[0].isupper() and string[1:].islower():
        return True
    return False


# 3
# asserts for pair_check
assert type(pair_check(1)) == bool, 'invalid type as a result of the function'
assert pair_check(1) is False, 'function logic error'
assert pair_check(2) is True, 'function logic error'
assert pair_check(0) is True, 'function logic error'
assert pair_check(-8) is True, 'function logic error'
assert pair_check(-7) is False, 'function logic error'
assert pair_check('2') is False, 'error in logic. If the get is not an int, the result will be False'
assert pair_check([1, 2]) is False, 'error in logic. If the get is not an int, the result will be False'

# assert for matching_capitalize
assert type(matching_capitalize('Hi bro')) is bool, 'invalid type as a result of the function'
assert matching_capitalize('Hi BRO') is False, 'function logic error'
assert matching_capitalize('Hi BRO') is False, 'function logic error'
assert matching_capitalize('Hi bro') is True, 'function logic error'
assert matching_capitalize('1hi bro') is False, 'function logic error, digit has no uppercase'
assert matching_capitalize(1) is False, 'logic error. If the get is not an str, the result will be False'
