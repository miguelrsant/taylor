import os
import uuid
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify
from middlewares.me_required import auth_required
from services.websocket.chat_services import chat_turn

chat_bp = Blueprint("chat", __name__, url_prefix="/chat")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
UPLOAD_DIR = os.path.join(BASE_DIR, "file_temps")


@chat_bp.post("/")
@auth_required
def index(user_id, session):
    message = (request.form.get("message") or "").strip()
    conversation_id = request.form.get("conversation_id")
    file = request.files.get("file")

    if not message:
        return jsonify({"msg": "Campo 'message' é obrigatório"}), 400

    savage_path = None
    orinal_filename = None

    if file and file.filename:
        orinal_filename = file.filename

        safae_name = secure_filename(file.filename) or "file"
        ext = os.path.splitext(safae_name)[1].lower()

        filename = f"{user_id}_{uuid.uuid4().hex}{ext}"
        savage_path = os.path.join(UPLOAD_DIR, filename)

        file.save(savage_path)

    result = chat_turn(
        user_id=user_id,
        conversation_id=conversation_id,
        user_message=message,
        file_path=savage_path if file else None,
        original_filename=orinal_filename if file else None,
    )

    return jsonify(result), 200
