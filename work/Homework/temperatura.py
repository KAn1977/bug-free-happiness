import requests

url = 'https://api.openweathermap.org/data/2.5/weather/'
params = {'q': 'Ташкент','appid':
          '72196223258f38a1815fa80718c2ef25', 'units':'metric', 'lang':'ru' }

weather = requests.get(url, params=params).json()
print(f'Погода в Ташкенте:\n{weather["weather"][0]["description"].title()}\n'
      f'Температура: {round(float(weather["main"]["temp"]))} градусов Цельсия.')