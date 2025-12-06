from database.connection import db
from datetime import datetime
from sqlalchemy.sql import func
import random
import string


def generate_id():
    return ''.join(random.choices(string.digits, k=7))


class PasswordReset(db.Model):
    id = db.Column(db.String(7), primary_key=True, default=generate_id)
    user_id = db.Column(db.Integer, nullable=False)
    token_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    used = db.Column(db.Boolean, default=False)
    revoked = db.Column(db.Boolean, default=False)
