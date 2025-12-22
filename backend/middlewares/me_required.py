import jwt
import bcrypt
import os
from flask import request, jsonify
from functools import wraps
from datetime import datetime, timezone
from database.connection import db
from database.models.sessions import Sessions
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
ISSUER = os.getenv("ISSUER")
AUDIENCE = os.getenv("AUDIENCE")


def auth_required(f):
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
        id = payload["sid"]
        truncated = token[:72]

        session = Sessions.query.filter_by(id=id, user_id=user_id).first()

        if not session:
            return jsonify({"msg": "Session not found"}), 401

        if not bcrypt.checkpw(truncated.encode("utf-8"), session.token_hash.encode("utf-8")):
            return jsonify({"msg": "Invalid session"}), 401

        if session.revoked:
            return jsonify({"msg": "Token revoked"}), 401

        expires_at = session.expires_at.replace(tzinfo=timezone.utc)

        if expires_at < datetime.now(timezone.utc):
            session.revoked = True
            db.session.commit()
            return jsonify({"msg": "Session expired"}), 401

        return f(user_id, session, *args, **kwargs)

    return decorated
