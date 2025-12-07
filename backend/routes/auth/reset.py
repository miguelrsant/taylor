from flask import Blueprint, request
from services.auth.reset_services import ResetPassword
from middlewares.reset_required import reset_required
reset_bp = Blueprint("reset", __name__, url_prefix="/reset")


@reset_bp.post("/")
@reset_required
def index():

    data = request.get_json()

    new_password = data["new_password"]

    return ResetPassword(new_password, user_id=request.user_id, id=request.id)
