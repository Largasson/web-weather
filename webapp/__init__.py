from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.python_org_news import get_python_news
from webapp.db import db
from webapp.user.models import User
from webapp.weather import weather_by_city
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as news_blueprint


def create_app():
    app = Flask(__name__)  # создаем Flask переменную (экземпляр класса Flask) и передаем в нее имя нашего файла
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
