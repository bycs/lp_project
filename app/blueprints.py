from app.admin.views import blueprint as admin
from app.articles.views import blueprint as articles
from app.user.views import blueprint as user


def init_blueprints(app):
    app.register_blueprint(admin)
    app.register_blueprint(articles)
    app.register_blueprint(user)
