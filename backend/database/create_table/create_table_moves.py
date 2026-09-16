from datetime import datetime

from extensions import db


class Move(db.Model):
    __tablename__ = "moves"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    game_id = db.Column(
        db.Integer,
        db.ForeignKey("games.id"),
        nullable=False
    )

    player_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    move_number = db.Column(
        db.Integer,
        nullable=False
    )

    move = db.Column(
        db.String(10),
        nullable=False
    )

    san = db.Column(
        db.String(20),
        nullable=False
    )

    fen = db.Column(
        db.String(100),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    game = db.relationship(
        "Game",
        foreign_keys=[game_id]
    )

    player = db.relationship(
        "User",
        foreign_keys=[player_id]
    )

    def __repr__(self):
        return f"<Move game={self.game_id} move={self.move_number}>"