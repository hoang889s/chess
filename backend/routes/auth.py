from flask import Blueprint, request, jsonify
from werkzeug.security import (generate_password_hash,check_password_hash)
from database.extensions import db
from database.create_table.create_table_users import User as Users
from utils.validator import (validate_username, validate_email, validate_password)
from flask_jwt_extended import (create_access_token,jwt_required,get_jwt_identity)
auth_bp = Blueprint(
    "auth", __name__, url_prefix="/api/auth"
)
# register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body không hợp lệ"
        }),400
    username = data.get("username","").strip()
    email = data.get("email","").strip().lower()
    password = data.get("password","")
    
    # 1 kiem tra du lieu bat buoc

    if not username:
        return jsonify({
            "success":False,
            "message": "Username không được để trống"
        }),400
    if not email:
        return jsonify({
            "success":False,
            "message": "Email không được để trống"
        }),400
    if not password:
        return jsonify({
            "success":False,
            "message": "Password không được để trống"
        }),400

    # 2 kiem tra validate du lieu
    if not validate_username(username):
        return jsonify({
            "success":False,
            "message": "Username phải từ 3-50 ký tự và chỉ chứa chữ, số, _"
        })
    if not validate_email(email):
        return jsonify({
            "success":False,
            "message": "Email không hợp lệ"
        })
    if not validate_password(password):
        return jsonify({
            "success":False,
            "message": "Password phải có ít nhất 8 ký tự"
        })
    # 3 kiem tra ton tai
    existing_user = Users.query.filter_by(
        username=username
    ).first()
    if existing_user:
        return jsonify({
            "success":False,
            "message": "Username đã tồn tại"
        }),409
    existing_email = Users.query.filter_by(
        email=email
    ).first()
    if existing_email:
        return jsonify({
            "success":False,
            "message": "Email đã được sử dụng"
        }),409
    #4 hash password
    password_hash = generate_password_hash(password)
    # 5 tao user moi
    user = Users(
        username=username,
        email=email,
        password_hash=password_hash,
        level=1,
        status=True,
        win = 0,
        lost = 0
    )
    try:
        db.session.add(user)
        db.session.commit()

    except Exception :
        db.session.rollback()
        return jsonify({
            "success":False,
            "message": "Đăng ký thất bại"
        }),500
    return jsonify({
        "success":True,
        "message": "Đăng ký thành công",
        "data":{
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "level": user.level,
            "status": user.status,
            "win": user.win,
            "lost": user.lost

        }
    }),201

# login
@auth_bp.route("/login", methods=["POST"])
def login():

    # 1. Lấy dữ liệu request
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body không hợp lệ"
        }), 400

    email = data.get("email", "").strip().lower()
    password = data.get("password", "")

    # 2. Kiểm tra dữ liệu bắt buộc
    if not email:
        return jsonify({
            "success": False,
            "message": "Email không được để trống"
        }), 400

    if not password:
        return jsonify({
            "success": False,
            "message": "Password không được để trống"
        }), 400

    # 3. Validate email
    if not validate_email(email):
        return jsonify({
            "success": False,
            "message": "Email không hợp lệ"
        }), 400

    # 4. Tìm user theo email
    user = Users.query.filter_by(
        email=email
    ).first()

    # Không tiết lộ email có tồn tại hay không
    if not user:
        return jsonify({
            "success": False,
            "message": "Email hoặc password không chính xác"
        }), 401

    # 5. Kiểm tra password
    if not check_password_hash(
        user.password_hash,
        password
    ):
        return jsonify({
            "success": False,
            "message": "Email hoặc password không chính xác"
        }), 401

    # 6. Kiểm tra trạng thái tài khoản
    if not user.status:
        return jsonify({
            "success": False,
            "message": "Tài khoản đã bị khóa"
        }), 403

    # 7. Tạo JWT Access Token
    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "username": user.username,
            "role": user.role
        }
    )

    # 8. Đăng nhập thành công
    return jsonify({
        "success": True,
        "message": "Đăng nhập thành công",
        "data": {
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "level": user.level,
                "status": user.status,
                "win": user.win,
                "lost": user.lost
            }
        }
    }), 200

# me
@auth_bp.route("/me" ,methods=["GET"])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity(user_id)
    user = Users.query.get(user_id)
    if not user:
        return jsonify({
            "success":False,
            "message":"Người dùng không tồn tại"
        }),404
    if not user.status:
        return jsonify({
            "success":False,
            "message": "Tài khoản đã bị khóa"
        }),403
    return jsonify({
        "success": True,
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "level": user.level,
            "status": user.status,
            "win": user.win,
            "lost": user.lost
        }
    }),200


