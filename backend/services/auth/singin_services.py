import jwt
import bcrypt
import os
from datetime import datetime, timedelta, timezone
from flask import jsonify
from database.models.user import User
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
EXPIRES_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES"))


def AcessLogin(email: str, password: str):
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401
    
    if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return jsonify({"msg": "Invalid credentials"}), 401
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRES_MINUTES)

    payload = {
        "sub": str(user.id),
        "exp": expire
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return jsonify({"token": token}), 200
