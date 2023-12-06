import requests


def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    param = {
        'key': 'fad2bca2211846118b8113642232711',
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'showlocaltime': 'yes',
        'lang': 'ru'
    }
    try:
        result = requests.get(weather_url, params=param)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException) as err:
        print(f'Сетевая ошибка - {err}')
        return False
    return False


if __name__ == '__main__':
    print(weather_by_city('Moscow,Russia'))

