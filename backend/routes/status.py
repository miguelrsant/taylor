from flask import Blueprint
from services.status_services import (
    get_version,
    get_max_connections,
    count_connections_to_maindb
)

status_bp = Blueprint("status", __name__, url_prefix="/status")


@status_bp.get("/")
def index():
    return {
        "db": {
            "version": get_version(),
            "max_connections": get_max_connections(),
            "opened_connections": count_connections_to_maindb()
        }
    }
