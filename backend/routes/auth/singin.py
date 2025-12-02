from flask import Blueprint, request
from services.auth.singin_services import AcessLogin

singin_bp = Blueprint("singin", __name__, url_prefix="/singin")


@singin_bp.post("/")
def index():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

    return AcessLogin(email, password)
