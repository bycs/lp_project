from flask import Blueprint

blueprint = Blueprint("home", __name__)


@blueprint.route("/")
def index_page():
    return "Home page (index)"
