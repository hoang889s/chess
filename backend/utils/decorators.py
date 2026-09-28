from functools import wraps

from flask import jsonify

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt
)


def role_required(*allowed_roles):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            # Kiểm tra JWT
            verify_jwt_in_request()

            # Lấy claims
            claims = get_jwt()

            # Lấy role
            role = claims.get("role")

            # Kiểm tra role
            if role not in allowed_roles:
                return jsonify({
                    "success": False,
                    "message": "Bạn không có quyền truy cập"
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator