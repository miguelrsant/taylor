from flask import Blueprint, request
from services.auth.recover_services import RecoverPass
recover_bp = Blueprint("recover", __name__, url_prefix="/recover")


@recover_bp.post("/")
def index():

    data = request.get_json()

    email = data["email"]

    return RecoverPass(email)
