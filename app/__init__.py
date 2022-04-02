from app.blueprints import init_blueprints
from app.config import APP_NAME, APP_SECRET_KEY, DB_URI, DEBUG
from app.config import db
from app.user.models import User

from flask import Flask, render_template

from flask_login import LoginManager

from flask_migrate import Migrate


def create_app():
    app = Flask(APP_NAME)
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = APP_SECRET_KEY

    app.debug = DEBUG

    init_blueprints(app)

    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user.login_page"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index_page():
        title = APP_NAME
        return render_template("index.html", page_title=title)

    return app


app = create_app()
