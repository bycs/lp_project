from app.user.forms import LoginForm, RegisterForm
from app.user.models import User
from app.user.utils import create_user

from flask import Blueprint, flash, redirect, render_template, url_for

from flask_login import current_user, login_user, logout_user

blueprint = Blueprint("user", __name__, url_prefix="/user")


@blueprint.route("/register")
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("index_page"))
    title = "Регистрация"
    form = RegisterForm()
    return render_template("user/register.html", page_title=title, form=form)


@blueprint.route("/process_register", methods=["POST"])
def process_register():
    form = RegisterForm()

    if form.validate_on_submit():
        create_user(form)
        flash("Вы успешно зарегистрировались :)")
        return redirect(url_for("user.login_page"))

    flash("Исправте ошибки в форме регистрации!")
    return redirect(url_for("user.register_page"))


@blueprint.route("/login")
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("index_page"))
    title = "Авторизация"
    form = LoginForm()
    return render_template("user/login.html", page_title=title, form=form)


@blueprint.route("/process_login", methods=["POST"])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_user.data)
            flash("Авторизация успешно пройдена")
            return redirect(url_for("index_page"))

    flash("Неправильный email или пароль!")
    return redirect(url_for("user.login_page"))


@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы успешно вышли")
    return redirect(url_for("index_page"))


@blueprint.route("/")
def user_page():
    return "Users page"
