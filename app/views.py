from app.config import APP_NAME

from flask import Blueprint, render_template

blueprint = Blueprint("home", __name__)


@blueprint.route("/")
def index_page():
    title = APP_NAME
    return render_template("index.html", page_title=title)
