import bcrypt
from datetime import datetime, timezone
from flask import jsonify
from database.connection import db
from database.models.user import User
from database.models.password_reset import PasswordReset
from database.models.sessions import Sessions
from core.email_client import email_client


def ResetPassword(new_password: str, user_id: str, id: str):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    hashed_password = bcrypt.hashpw(new_password.encode(
        "utf-8"), bcrypt.gensalt()).decode("utf-8")

    user.password = hashed_password

    Sessions.query.filter_by(user_id=user_id).delete()
    password_reset = PasswordReset.query.get(id)
    password_reset.used = True
    db.session.commit()

    html_content = f"""
        <h1>Senha Redefinida com Sucesso</h1>
        <p>Olá <strong>{user.name}</strong>,</p>
        <p>Sua senha foi redefinida com sucesso.</p>
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


    return jsonify({"msg": "Password reset successful"}), 200
