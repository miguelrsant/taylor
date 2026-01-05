from flask import Blueprint, request, jsonify
from middlewares.me_required import auth_required
from services.websocket.chat_services import chat_turn

chat_bp = Blueprint("chat", __name__, url_prefix="/chat")


@chat_bp.post("/")
@auth_required
def index(user_id, session):
    data = request.get_json(force=True) or {}

    message = (data.get("message") or "").strip()
    conversation_id = data.get("conversation_id")

    if not message:
        return jsonify({"msg": "Campo 'message' é obrigatório"}), 400

    result = chat_turn(
        user_id=user_id,
        conversation_id=conversation_id,
        user_message=message,
    )

    return jsonify(result), 200
