from database.connection import db
from sqlalchemy.sql import func
import uuid


def uuid_str():
    return str(uuid.uuid4())


class Conversations(db.Model):
    __tablename__ = "conversations"

    id = db.Column(db.String(36), primary_key=True, default=uuid_str)
    user_id = db.Column(db.Integer, nullable=False, index=True)

    title = db.Column(db.String(120), nullable=True)

    created_at = db.Column(
        db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
