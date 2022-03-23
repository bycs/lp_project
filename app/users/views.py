from flask import Blueprint

blueprint = Blueprint("users", __name__, url_prefix="/user")


@blueprint.route("/")
def user_page():
    return "Users page"
