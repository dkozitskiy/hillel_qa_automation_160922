'''
1. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Зауважте, що lst1 не є статичним і може формуватися динамічно.

2. Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]. Напишіть код,
який видалить з нього всі числа, які менше 21 і більше 74.

3. Є стрінг з певним текстом (можна скористатися input або константою). Напишіть код, який визначить
кількість слів в цьому тексті, які закінчуються на 'о'.
'''

# 1
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for lst_value in lst1:
    if type(lst_value) is str:
        lst2.append(lst_value)
print(lst2)

# 2
lst_num = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
lst_temp = lst_num.copy()
for num in lst_temp:
    if num < 21 or num > 74:
        lst_num.remove(num)
print(lst_num)

# 3
count = 0
some_text = input('Напишите произвольный текст кирилицей\n')
some_text.lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '').replace('\'', '').split()
for i in some_text:
    if i[-1] == 'о':
        count += 1
print(f'Слов которые заканчиваются на \'о\' в тексте {count} ')
