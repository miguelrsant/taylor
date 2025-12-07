import os
from datetime import datetime, timezone
import jwt
import bcrypt
from database.models import Sessions
from database.connection import db
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
ISSUER = os.getenv("ISSUER")
AUDIENCE = os.getenv("AUDIENCE")


def LogoutToken(session_token: str) -> dict:

    try:
        payload = jwt.decode(
            session_token,
            SECRET,
            algorithms=["HS256"],
            issuer=ISSUER,
            audience=AUDIENCE
        )
    except jwt.ExpiredSignatureError:
        return {"msg": "Token expired"}, 401
    except jwt.InvalidTokenError:
        return {"msg": "Invalid token"}, 401

    truncated = session_token[:72]
    session_id = payload["sid"]

    session = Sessions.query.filter_by(id=session_id).first()

    if not session:
        return {"msg": "Session not found"}

    if not bcrypt.checkpw(truncated.encode("utf-8"), session.token_hash.encode("utf-8")):
        return {"msg": "Invalid session"}

    Sessions.query.filter_by(id=session_id).delete()
    db.session.commit()
    return {"msg": "Logout successful"}, 200
