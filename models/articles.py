import uuid

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.dialects.postgresql import UUID


db = SQLAlchemy()


class CategoryArticle(db.Model):
    __tablename__ = "categories_articles"
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    title = db.Column(db.String(20), unique=True, nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    is_show = db.Column(db.Boolean, default=False, nullable=False)
    author_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    def __repr__(self):
        return f"<Article id={self.id}, {self.title}>"


class AccessArticlesRule(db.Model):
    __tablename__ = "access_articles_rules"
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False
    )
    article_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("articles.id", ondelete="CASCADE"),
        nullable=False,
    )
