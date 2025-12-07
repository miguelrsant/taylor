from flask import Blueprint, request
from services.auth.logout_services import LogoutToken
logout_bp = Blueprint("logout", __name__, url_prefix="/logout")


@logout_bp.post("/")
def index():

    data = request.get_json()
    session_token = data.get("session_token")
    return LogoutToken(session_token)
