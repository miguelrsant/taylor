import jwt
import bcrypt
import os
from datetime import datetime, timedelta, timezone
from flask import jsonify
from database.connection import db
from database.models.user import User
from database.models.sessions import Sessions
from database.models.sessions import generate_id
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
EXPIRES_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES"))
ISSUER = os.getenv("ISSUER")
AUDIENCE = os.getenv("AUDIENCE")


def hash_token(token) -> str:
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    truncated = token[:72]

    return bcrypt.hashpw(truncated.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def AcessLogin(email: str, password: str):
    sid = generate_id()
    user = User.query.filter_by(email=email, is_active=True).first()

    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return jsonify({"msg": "Invalid credentials"}), 401

    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRES_MINUTES)

    payload = {
        "sub": str(user.id),
        "sid": sid,
        "iss": ISSUER,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "aud": AUDIENCE,
        "exp": expire
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    if isinstance(token, bytes):
        token = token.decode("utf-8")

    token_hash = hash_token(token)

    new_session = Sessions(
        id=sid,
        user_id=user.id,
        token_hash=token_hash,
        expires_at=expire,
        revoked=False
    )

    db.session.add(new_session)

    user.last_login = datetime.now(timezone.utc)

    db.session.commit()

    response = jsonify({"token": token})
    response.status_code = 200

    response.set_cookie(
        "token",
        token,
        httponly=True,
        secure=False,
        samesite="Lax"
    )

    return response, 200