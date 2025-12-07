import bcrypt
from datetime import datetime, timezone
from flask import jsonify
from database.connection import db
from database.models.user import User
from database.models.password_reset import PasswordReset
from database.models.sessions import Sessions


def ResetPassword(new_password: str, user_id: str, password_reset_obj):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    hashed_password = bcrypt.hashpw(new_password.encode(
        "utf-8"), bcrypt.gensalt()).decode("utf-8")

    user.password = hashed_password

    Sessions.query.filter_by(user_id=user_id).delete()
    password_reset = PasswordReset.query.get(password_reset_obj.id)
    password_reset.used = True
    db.session.commit()

    return jsonify({"msg": "Password reset successful"}), 200
