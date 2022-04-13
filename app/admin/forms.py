from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class RoleForm(FlaskForm):
    role = StringField(
        "Имя роли пользователя",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    role2 = StringField(
        "Повтор роли",
        validators=[DataRequired(), EqualTo("role")],
        render_kw={"class": "form-control"},
    )

    submit = SubmitField("Добавить роль", render_kw={"class": "btn btn-primary"})
