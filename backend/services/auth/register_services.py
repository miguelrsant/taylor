from flask import jsonify
import bcrypt
from database.connection import db
from database.models.user import User

def CreateRegister(name: str, email: str, password: str):
    existing = User.query.filter_by(email=email).first()

    if existing:
        return jsonify({"msg": "Email already exists"}), 400

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    user = User (
        name=name,
        email=email,
        password=hashed
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201