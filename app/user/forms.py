from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Пароль", validators=[DataRequired()], render_kw={"class": "form-control"}
    )
    password2 = PasswordField(
        "Повтор пароля",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"class": "form-control"},
    )
    first_name = StringField(
        "Имя", validators=[DataRequired()], render_kw={"class": "form-control"}
    )
    middle_name = StringField("Отчество", render_kw={"class": "form-control"})
    last_name = StringField(
        "Фамилия", validators=[DataRequired()], render_kw={"class": "form-control"}
    )
    submit = SubmitField("Зарегистрироваться", render_kw={"class": "btn btn-primary"})


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        label="Пароль", validators=[DataRequired()], render_kw={"class": "form-control"}
    )
    remember_user = BooleanField(
        "Запомнить меня", default=True, render_kw={"class": "form-check-input"}
    )
    submit = SubmitField("Войти", render_kw={"class": "btn btn-primary"})
