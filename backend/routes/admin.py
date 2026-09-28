from flask import Blueprint,jsonify
from utils.decorators import role_required
admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/api/admin"
)
@admin_bp.route("/users", methods=["GET"])
@role_required("admin")
def get_users():

    return jsonify({
        "success": True,
        "message": "Bạn là admin"
    }), 200