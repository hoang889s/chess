from datetime import datetime

from extensions import db


class RoomPlayer(db.Model):
    __tablename__ = "room_players"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    joined_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    left_at = db.Column(
        db.DateTime,
        nullable=True
    )

    __table_args__ = (
        db.UniqueConstraint(
            "room_id",
            "user_id",
            name="uq_room_player"
        ),
    )

    room = db.relationship(
        "Room",
        foreign_keys=[room_id]
    )

    user = db.relationship(
        "User",
        foreign_keys=[user_id]
    )

    def __repr__(self):
        return f"<RoomPlayer room={self.room_id} user={self.user_id}>"