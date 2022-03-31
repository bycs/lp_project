from app.admin.views import blueprint as admin
from app.articles.views import blueprint as articles
from app.config import APP_NAME, APP_SECRET_KEY, DB_URI, DEBUG
from app.db import db
from app.users.models import User
from app.users.views import blueprint as users
from app.views import blueprint as home

from flask import Flask

from flask_login import LoginManager

from flask_migrate import Migrate


def create_app():
    app = Flask(APP_NAME)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = APP_SECRET_KEY

    app.debug = DEBUG

    app.register_blueprint(admin)
    app.register_blueprint(home)
    app.register_blueprint(articles)
    app.register_blueprint(users)

    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "home.login_page"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
