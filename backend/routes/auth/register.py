from flask import Blueprint, request
from services.auth.register_services import CreateRegister

register_bp = Blueprint("register", __name__, url_prefix="/register")


@register_bp.post("/")
def index():
    data = request.get_json()

    name = data["name"]
    email  = data["email"]
    password = data["password"]

    return  CreateRegister(name, email, password)
