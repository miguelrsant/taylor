from flask import jsonify
import bcrypt
from database.connection import db
from database.models.user import User
from core.email_client import email_client
from services.auth.singin_services import AcessLogin


def CreateRegister(name: str, email: str, password: str):
    existing = User.query.filter_by(email=email).first()

    if existing:
        return jsonify({"msg": "Email already exists"}), 400

    hashed = bcrypt.hashpw(password.encode(
        "utf-8"), bcrypt.gensalt()).decode("utf-8")

    user = User(
        name=name,
        email=email,
        password=hashed
    )

    db.session.add(user)
    db.session.commit()

    html_content = f"""
    <h1>Obrigado por se registrar no Taylor!</h1>
    <p>Olá <strong>{user.name}</strong>,</p>
    <p>Seu cadastro foi realizado com sucesso. Em breve você receberá novidades e atualizações diretamente no seu e-mail.</p>
    <p>— Equipe Taylor</p>
    """

    try:
        email_client.send_email(
            to=user.email,
            subject="Você agora está no TAYLOR",
            html=html_content
        )
    except Exception as email_error:
        print(f"Erro ao enviar email: {email_error}")

    login_response, status = AcessLogin(email, password)

    if status != 200:
        return login_response, status

    token = login_response.get_json()["token"]

    response = jsonify({"msg": "User created", "token": token})
    response.status_code = 201

    response.set_cookie(
        "token",
        token,
        httponly=True,
        secure=False,
        samesite="Lax"
    )

    return response
