'''
1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
Слово та номер отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

2. Написати цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви о.
'''

# №1
word, character_num = input('Write a word\n'), input('Write the ordinal number of the word to search\n')
try:
    print(f'The {character_num} symbol in {word} is \'{word[int(character_num)-1]}\'')
except ValueError:
    print('Error! Specify the character number as a number')
except IndexError:
    print('There is no way to find a symbol with this number')

# №2
while True:
    word_with_o = input('Write a word that contains the letter \'o\' (Latin or Cyrillic)\n').lower()
    if 'o' in word_with_o or 'о' in word_with_o:
        print('Thanks')
        break
    else:
        print('Missing letter in word')
