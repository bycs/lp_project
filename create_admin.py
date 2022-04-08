import sys
from getpass import getpass

from app.config import db
from app.user.models import User

from wsgi import app


def create_admin():
    with app.app_context():
        email = input("Введите e-mail: ")

        if User.query.filter(User.email == email).count():
            print("Пользователь с таким e-mail уже зарегистрирован!")
            sys.exit(0)

        password1 = getpass("Введите пароль: ")
        password2 = getpass("Повторите пароль: ")

        if password1 != password2:
            print("Пароли не совпадают!")
            sys.exit(0)
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        last_name = input("Введите фамилию: ")

        new_admin = User(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            is_verification=True,
            is_admin=True,
        )

        new_admin.set_password(password1)
        db.session.add(new_admin)
        db.session.commit()
        print(f"Пользователь {new_admin} успешно создан.")


if __name__ == "__main__":
    create_admin()
