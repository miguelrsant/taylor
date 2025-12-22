import jwt
import bcrypt
import os
from datetime import datetime, timedelta, timezone
from flask import jsonify
from database.connection import db
from database.models.user import User
from database.models.password_reset import PasswordReset
from database.models.password_reset import generate_id
from core.email_client import email_client
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
EXPIRES_MINUTES_PASSWORD_RESET = int(
    os.getenv("EXPIRES_MINUTES_PASSWORD_RESET"))
ISSUER = os.getenv("ISSUER")
AUDIENCE = os.getenv("AUDIENCE")


def hash_token(token) -> str:
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    truncated = token[:72]

    return bcrypt.hashpw(truncated.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def RecoverPass(email: str):
    user = User.query.filter_by(email=email, is_active=True).first()
    sid = generate_id()
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=EXPIRES_MINUTES_PASSWORD_RESET)

    payload = {
        "sid": sid,
        "sub": str(user.id),
        "iss": ISSUER,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "aud": AUDIENCE,
        "exp": expire
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    if isinstance(token, bytes):
        token = token.decode("utf-8")

    token_hash = hash_token(token)

    new_password_reset = PasswordReset(
        id=sid,
        user_id=user.id,
        token_hash=token_hash,
        expires_at=expire,
        used=False,
        revoked=False
    )

    html_content = f"""
        <h1>Recuperação de Senha</h1>
        <p>Olá <strong>{user.name}</strong>,</p>
        <p>Recebemos uma solicitação para redefinir sua senha. Se você não fez essa solicitação, por favor, ignore este e-mail.</p>
        <p>Para redefinir sua senha, clique no link abaixo:</p>
        <p><a href="https://taylorhub.com.br/reset-password?token={token}">Redefinir Senha</a></p>
        <p>Este link expirará em {EXPIRES_MINUTES_PASSWORD_RESET} minutos.</p>
        <p>— Equipe Taylor</p>
        """

    try:
        email_client.send_email(
            to=user.email,
            subject="RECUPERAÇÃO DE SENHA - TAYLOR",
            html=html_content
        )
    except Exception as email_error:
        print(f"Erro ao enviar email: {email_error}")

    db.session.add(new_password_reset)

    db.session.commit()

    return jsonify({"status": "Email Enviado"}), 200
