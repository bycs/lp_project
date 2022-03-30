from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = StringField("e-mail", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    first_name = StringField("Имя", validators=[DataRequired()])
    middle_name = StringField("Отчество", validators=[DataRequired()])
    last_name = StringField("Фамилия", validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    email = StringField("e-mail", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_user = BooleanField(
        "Запомнить меня", default=True, render_kw={"class": "form-check-input"}
    )
    submit = SubmitField("Войти")
