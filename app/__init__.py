from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import APP_NAME, DB_URI, APP_SECRET_KEY, DEBUG
from app.views import blueprint as home
from app.users.views import blueprint as users


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(APP_NAME)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = APP_SECRET_KEY
    app.register_blueprint(home)
    app.register_blueprint(users)
    app.debug = DEBUG
    db.init_app(app)
    migrate.init_app(app, db)

    return app
