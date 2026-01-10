from database.connection import db
from sqlalchemy.sql import func
import uuid


def uuid_str():
    return str(uuid.uuid4())


class Messages(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.String(36), primary_key=True, default=uuid_str)
    conversation_id = db.Column(
        db.String(36),
        db.ForeignKey("conversations.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    role = db.Column(db.String(16), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file_path = db.Column(db.String(255), nullable=True)
    original_filename = db.Column(db.String(255), nullable=True)

    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)
