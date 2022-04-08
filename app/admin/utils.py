from app.user.models import User


def get_all_users():
    users = User.query.order_by(User.is_verification, User.email).all()
    return users


if __name__ == "__main__":
    get_all_users()
