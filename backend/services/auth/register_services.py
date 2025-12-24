from flask import jsonify
import bcrypt
from database.connection import db
from database.models.user import User
from jobs.queue import queue
from jobs.tasks import send_email_register
from rq import Retry
from services.auth.signin_services import AcessLogin


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

    try:

        job = queue.enqueue(
            send_email_register,
            email,
            name,
            job_timeout=120,
            retry=Retry(max=3, interval=[10, 60, 300])
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
