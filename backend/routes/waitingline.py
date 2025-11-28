from flask import Blueprint, request, jsonify
from services.waitingline_services import add_user_to_waiting_line

waitingline_bp = Blueprint('waitingline', __name__, url_prefix='/waitingline')


@waitingline_bp.route('/', methods=['POST'])
def handle_waiting_line_submission():
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "status": "error",
            "message": "Dados inválidos. 'name' e 'email' são obrigatórios."
        }), 400

    name = data['name']
    email = data['email']

    result = add_user_to_waiting_line(name, email)

    if result["status"] == "success":
        return jsonify(result), 201
    else:
        status_code = 400 if "e-mail fornecido já está" in result["message"] else 500
        return jsonify(result), status_code
