import jwt
import bcrypt
import os
from datetime import datetime, timedelta, timezone
from flask import jsonify, request, session
from functools import wraps
from database.connection import db
from database.models.user import User
from database.models.password_reset import PasswordReset
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
ISSUER = os.getenv("ISSUER")
AUDIENCE = os.getenv("AUDIENCE")


def reset_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"msg": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(
                token,
                SECRET,
                algorithms=["HS256"],
                issuer=ISSUER,
                audience=AUDIENCE
            )
        except jwt.ExpiredSignatureError:
            return jsonify({"msg": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"msg": "Invalid token"}), 401

        user_id = payload["sub"]

        truncated = token[:72]

        password_reset = PasswordReset.query.filter_by(
            user_id=user_id, used=False, revoked=False).first()

        if not password_reset:
            return jsonify({"msg": "Token not found"}), 401

        if not bcrypt.checkpw(truncated.encode("utf-8"), password_reset.token_hash.encode("utf-8")):
            return jsonify({"msg": "Invalid Token"}), 401

        if password_reset.used:
            return jsonify({"msg": "Token used"}), 401

        if password_reset.revoked:
            return jsonify({"msg": "Token revoked"}), 401

        expires_at = password_reset.expires_at.replace(tzinfo=timezone.utc)

        if expires_at < datetime.now(timezone.utc):
            password_reset.revoked = True
            db.session.commit()
            return jsonify({"msg": "Token expired"}), 401

        request.user_id = user_id
        request.password_reset_obj = password_reset

        return f(*args, **kwargs)
    return decorated
