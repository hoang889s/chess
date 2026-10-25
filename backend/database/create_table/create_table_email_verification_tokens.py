from ..extensions import db
class EmailVerificationToken(db.Model):
    __tablename__ = "email_verification_tokens"
    id  = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    # chi luu gia tri bam token
    token_hash = db.Column(
        db.String(64),
        nullable=False,
        unique=True

    )
    expires_at = db.Column(
        db.DateTime,
        nullable=False
    )
    used_at = db.Column(
        db.DateTime,
        nullable=True

    )
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.current_timestamp()
    )
    user = db.relationship(
        "User",
        backref=db.backref("email_verification_tokens",lazy=True)
    )