from app.admin.decorators import admin_required
from app.admin.utils import get_all_users

from flask import Blueprint, render_template

blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("/")
@admin_required
def admin_page():
    title = "Панель управления"
    return render_template("admin/index.html", page_title=title)


@blueprint.route("/users")
@admin_required
def users_list():
    users = get_all_users()
    title = "Список пользователей"
    return render_template("admin/users.html", page_title=title, users=users)
