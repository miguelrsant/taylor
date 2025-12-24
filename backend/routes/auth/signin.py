from flask import Blueprint, request
from services.auth.signin_services import AcessLogin

signin_bp = Blueprint("signin", __name__, url_prefix="/signin")


@signin_bp.post("/")
def index():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

    return AcessLogin(email, password)
