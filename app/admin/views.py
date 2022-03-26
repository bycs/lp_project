from flask import Blueprint

from flask_login import current_user, login_required


blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("/")
@login_required
def admin_page():
    if current_user.is_admin:
        return "Добро пожаловать, Админ"
    else:
        return "Ты не админ!"