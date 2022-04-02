import os

from flask_sqlalchemy import SQLAlchemy

DEBUG = os.getenv("DEBUG", False)

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY", "XXX")
APP_NAME = os.getenv("APP_NAME", "__name__")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = os.getenv("APP_PORT", "5000")

DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "pass")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))
DB_NAME = os.getenv("POSTGRES_DB", "db")
DB_URI = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

db = SQLAlchemy()
