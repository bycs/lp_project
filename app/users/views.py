from flask import Blueprint

blueprint = Blueprint("users", __name__, url_prefix="/users")


@blueprint.route("/")
def index_page():
    return "Users page"
