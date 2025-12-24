import bcrypt
from datetime import datetime, timezone
from flask import jsonify
from database.connection import db
from database.models.user import User
from database.models.password_reset import PasswordReset
from database.models.sessions import Sessions
from jobs.queue import queue
from jobs.tasks import send_email_reset
from rq import Retry


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

    try:
        job = queue.enqueue(
            send_email_reset,
            user.email,
            name=user.name,
            job_timeout=120,
            retry=Retry(max=3, interval=[10, 60, 300])
        )
    
    except Exception as email_error:
        print(f"Erro ao enviar email: {email_error}")


    return jsonify({"msg": "Password reset successful"}), 200
