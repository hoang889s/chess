from datetime import datetime
from extensions import db
class Room(db.Model):
    __tablename__ = "rooms"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    room_code = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    game_id = db.Column(
        db.Integer,
        db.ForeignKey("games.id"),
        nullable=True
    )

    lock = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    owner = db.relationship(
        "User",
        foreign_keys=[owner_id]
    )

    game = db.relationship(
        "Game",
        foreign_keys=[game_id]
    )

    def __repr__(self):
        return f"<Room {self.room_code}>"