from flask import Blueprint

from app.admin.decorators import admin_required

blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("/")
@admin_required
def admin_page():
    return "Добро пожаловать, Админ"

