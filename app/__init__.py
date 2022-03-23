from app.articles.views import blueprint as articles
from app.config import APP_NAME, APP_SECRET_KEY, DB_URI, DEBUG
from app.users.views import blueprint as users
from app.views import blueprint as home

from flask import Flask

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(APP_NAME)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = APP_SECRET_KEY

    app.debug = DEBUG

    app.register_blueprint(home)
    app.register_blueprint(articles)
    app.register_blueprint(users)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app()
