'''
завдання 1
урл http://api.open-notify.org/astros.json
вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)

завдання 2
апі погоди (всі токени я для вас вже прописав)
https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
результатом буде приблизно такий результат
{"coord":{"lon":30.7326,"lat":46.4775},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"stations",
"main":{"temp":13.94,"feels_like":12.8,"temp_min":13.94,"temp_max":13.94,"pressure":1021,"humidity":54,"sea_level":1021,"grnd_level":1015},
"visibility":10000,"wind":{"speed":4.58,"deg":314,"gust":8.16},"clouds":{"all":73},"dt":1664909335,"sys":{"country":"UA","sunrise":1664855942,"sunset":1664897549},
"timezone":10800,"id":698740,"name":"Odesa","cod":200}
погода змінюється, як і місто. яке ви введете
'''

import requests

# 1
astronauts = requests.get('http://api.open-notify.org/astros.json').json()['people']
print('Перечень астронавтов на орбите на момент запроса:')
for astronaut in astronauts:
    print(astronaut['name'])

# 2
city_name = input('Укажите город на англ\n')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
response = requests.get(url).json()
try:
    print(f'''
    Погода в городе {city_name}:
    - Облачность: {response['weather'][0]['description']}
    - Температура воздуха: {response['main']['temp']}°C
    - Ощущается как: {response['main']['feels_like']}°C
    - Скорость ветра: {response['wind']['speed']}
    - Влажность: {response['main']['humidity']}
    ''')
except KeyError:
    print('Моя твоя не понимать. Проверь название города')
