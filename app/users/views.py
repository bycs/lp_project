from app import User
from app.db import db
from app.users.forms import LoginForm, RegisterForm
from app.views import blueprint as home

from flask import Blueprint, flash, redirect, render_template, url_for

from flask_login import current_user, login_user, logout_user

blueprint = Blueprint("users", __name__, url_prefix="/user")


@home.route("/register")
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("home.index_page"))
    title = "Регистрация"
    form = RegisterForm()
    return render_template("register.html", page_title=title, form=form)


@home.route("/process_register", methods=["POST"])
def process_register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            middle_name=form.middle_name.data,
            last_name=form.last_name.data,
        )

        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Вы успешно зарегистрировались")
        return redirect(url_for("home.login_page"))

    flash("Исправте ошибки в форме регистрации!")
    return redirect(url_for("home.register_page"))


@home.route("/login")
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("home.index_page"))
    title = "Авторизация"
    form = LoginForm()
    return render_template("login.html", page_title=title, form=form)


@home.route("/process_login", methods=["POST"])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_user.data)
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
