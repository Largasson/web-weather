from flask import Flask
from weather import weather_by_city

app = Flask(__name__)  # создаем Flask переменную (экземпляр класса Flask) и передаем в нее имя нашего файла


@app.route('/')  # функция, идущая следом за url-запросом. url - запрос / - означает главная страница
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        weather_text = f"Температура в городе: {weather['temp_C']} градуса Цельсия (ощущается как {weather['FeelsLikeC']})"
    else:
        weather_text = "Сервис погоды временно не доступен"
    return f"""
    <html>
        <head>
            <title>Прогноз погоды</title>
        </head>
        <body>
            <h1>{weather_text}</h2>
            <ol>
                <li>Один</li>
                <li>Два</li>
                <li>Три</li>
            </ol>
        </body>
    </html>
    """




if __name__ == '__main__':
    app.run(debug=True)
