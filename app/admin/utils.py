from app.config import db
from app.user.models import Role, User


def get_all_users():
    users = User.query.order_by(User.is_verification, User.email).all()
    return users


def verification_user(user_id, status):
    db.session.query(User).filter(User.id == user_id).update({"is_verification": status})
    db.session.commit()


def create_role(form):
    new_role = Role(role_name=form.role.data)

    db.session.add(new_role)
    db.session.commit()
