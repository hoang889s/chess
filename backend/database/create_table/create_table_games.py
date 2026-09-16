from datetime import datetime

from extensions import db


class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    white_player_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    black_player_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    fen = db.Column(
        db.String(100),
        nullable=False
    )

    pgn = db.Column(
        db.Text,
        nullable=True
    )

    start_time = db.Column(
        db.DateTime,
        nullable=True
    )

    end_time = db.Column(
        db.DateTime,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    white_player = db.relationship(
        "User",
        foreign_keys=[white_player_id]
    )

    black_player = db.relationship(
        "User",
        foreign_keys=[black_player_id]
    )

    def __repr__(self):
        return f"<Game {self.id}>"