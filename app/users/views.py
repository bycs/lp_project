from app import User
from app.users.forms import LoginForm
from app.views import blueprint as home

from flask import Blueprint, flash, redirect, render_template, url_for

from flask_login import current_user, login_user, logout_user


blueprint = Blueprint("users", __name__, url_prefix="/user")


@home.route("/login")
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("home.index_page"))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template("login.html", page_title=title, form=login_form)


@home.route("/process_login", methods=["POST"])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Авторизация успешно пройдена")
            return redirect(url_for("home.index_page"))

    flash("Неправильный e-mail или пароль!")
    return redirect(url_for("home.login_page"))


@home.route("/logout")
def logout():
    logout_user()
    flash("Вы успешно вышли")
    return redirect(url_for("home.index_page"))


@blueprint.route("/")
def user_page():
    return "Users page"
