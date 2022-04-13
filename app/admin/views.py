from app.admin.decorators import admin_required
from app.admin.utils import get_all_users, verification_user

from flask import Blueprint, flash, redirect, render_template, request, url_for

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


@blueprint.route("/verification_users")
@admin_required
def verification_users_page():
    users = get_all_users()
    title = "Подтверждение пользователей"
    return render_template(
        "admin/verification_users.html", page_title=title, users=users
    )


@admin_required
@blueprint.route("/process_verification_users")
def process_verification_users():
    user_id = request.values.get("user_id")
    status = bool(request.values.get("is_verification"))
    verification_user(user_id, status)
    flash("Статус пользователя успешно изменен")
    return redirect(url_for("admin.users_list"))
