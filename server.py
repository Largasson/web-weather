from flask import Flask
from weather import weather_by_city

app = Flask(__name__)  # создаем Flask переменную (экземпляр класса Flask) и передаем в нее имя нашего файла


@app.route('/')  # функция, идущая следом за url-запросом. url - запрос / - означает главная страница
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        return f"Температура в городе: {weather['temp_C']} градуса Цельсия (ощущается как {weather['FeelsLikeC']})"
    else:
        return "Сервис погоды временно не доступен"


if __name__ == '__main__':
    app.run(debug=True)


 #изменение