from flask import Blueprint
singin_bp = Blueprint("singin", __name__, url_prefix="/singin")


@singin_bp.post("/")
def index():
    return {
        "singin": "ok",
    }
