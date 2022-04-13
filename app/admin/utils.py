from app.config import db
from app.user.models import User


def get_all_users():
    users = User.query.order_by(User.is_verification, User.email).all()
    return users


def verification_user(user_id, status):
    db.session.query(User).filter(User.id == user_id).update(
        {"is_verification": status}
    )
    db.session.commit()


if __name__ == "__main__":
    get_all_users()
