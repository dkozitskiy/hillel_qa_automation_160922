'''
1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві
голосні літери підряд.

2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
"buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}.
Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між
мінімальною і максимальною ціною. Наприклад:
lower_limit = 35.9
upper_limit = 37.339
> match: "x-store", "main-service"
'''

# 1
text = input('Напишите произвольные слова на русском\n').lower().split()
vowels_list = ('а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
count_word = 0
for word in text:
    count_vowels = 0
    for letter in word:
        if letter in vowels_list:
            count_vowels += 1
        else:
            count_vowels = 0
        if count_vowels == 2:
            count_word += 1
            break
print(f'{count_word} слов с двумя гласными подряд в строке')

# 2
lower_limit = 35.9
upper_limit = 37.339
price = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,
         "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}
shops_by_criterion = []
for shop in price.items():
    if lower_limit < shop[1] < upper_limit:
        shops_by_criterion.append(shop[0])
print("Отсортированные магазины: " + ', '.join(shops_by_criterion))
