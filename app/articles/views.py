from flask import Blueprint

blueprint = Blueprint("articles", __name__, url_prefix="/article")


@blueprint.route("/")
def article_page():
    return "Articles page"
