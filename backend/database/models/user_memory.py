from database.connection import db
from sqlalchemy.sql import func
import random, string

def generate_id():
    return ''.join(random.choices(string.digits, k=7))

class UserMemory(db.Model):
    __tablename__ = "user_memory"

    id = db.Column(db.String(7), primary_key=True, default=generate_id)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    memory_text = db.Column(db.Text, nullable=False, default="")
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
