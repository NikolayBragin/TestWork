import requests

def exchange_rate():
    response = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/')
    usd = float(response.json()[0]['Rate'])
    eur = float(response.json()[1]['Rate'])
    rub = float(response.json()[2]['Rate'])
    funt = float(response.json()[3]['Rate'])
    iyena = float(response.json()[4]['Rate'])
    real = float(response.json()[11]['Rate'])
    print(f'Курс Американского доллара (USD) = {usd} сум (UZC)')
    print(f'Курс Евро (EUR) = {eur} сум (UZC)')
    print(f'Курс Российского рубля (RUB) = {rub} сум (UZC)')
    print(f'Курс Английского фунта стерлингов (GBP) = {funt} сум (UZC)')
    print(f'Курс Японской иены (JPY) = {iyena} сум (UZC)')
    print(f'Курс Бращильского реала> (BRL) = {real} сум (UZC)')
def get_weather(city):
    API_TOKEN = '7d58c54b3c0c66b13dcff13b9c5134e7'
    params = {'q': city, 'appid': API_TOKEN, 'units': 'metric'}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    x = response.json()
    if x['weather'][0]['main'] == 'Clear':
        p = 'ясно'
    else:
        p = 'облачно'
    print(f'Сегодня в городе {city} {p}')
    print('Температура:', x['main']['temp'], 'Градусов Цельсия')
    print('Атмосферное давление:', x['main']['pressure'], 'мм. рт. ст.')
    print('Влажность:', x['main']['humidity'], '%')
    print('Скорость ветра:', x['wind']['speed'], 'м/сек')

while True:
    print('')
    main = int(input('Если хотите узнать погоду нажмите 1. Если хотите узнать текущий курс шести основных валют нажмите 2: '))
    if main == 1:
        city = input('Введите город: ')
        get_weather(city)
    elif main == 2:
        exchange_rate()
    else:
        print('Неверный выбор, дружище :)')
