import uuid

from app import db

from sqlalchemy.dialects.postgresql import UUID


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    email = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    middle_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15), nullable=False)
    is_verification = db.Column(db.Boolean, default=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    @property
    def fullname(self):
        if self.middle_name is None:
            return f"{self.last_name} {self.first_name}"
        return f"{self.last_name} {self.middle_name} {self.first_name}"

    def __repr__(self):
        return f"<User id={self.id}, {self.fullname}>"


class RoleUser(db.Model):
    __tablename__ = "roles_users"
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False
    )
    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
