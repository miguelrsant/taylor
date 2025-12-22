from flask import Blueprint, jsonify
from database.models.user import User
from middlewares.me_required import auth_required

me_route = Blueprint("me", __name__)


@me_route.route("/me", methods=["GET"])
@auth_required
def get_me(user_id, session):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "session": {
            "id": session.id,
    }
    }), 200
