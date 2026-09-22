from ..extensions import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    username = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    level = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    status = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    win = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    lost = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False
    )