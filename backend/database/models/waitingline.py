from database.connection import db
from sqlalchemy.sql import func
import random
import string

def generate_id():
    return ''.join(random.choices(string.digits, k=7))

class Waitingline(db.Model):
    id = db.Column(db.String(7), primary_key=True, default=generate_id)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
