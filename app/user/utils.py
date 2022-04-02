from app.config import db
from app.user.models import User


def create_user(form):
    new_user = User(
        email=form.email.data,
        first_name=form.first_name.data,
        middle_name=form.middle_name.data,
        last_name=form.last_name.data,
    )

    new_user.set_password(form.password.data)
    db.session.add(new_user)
    db.session.commit()
