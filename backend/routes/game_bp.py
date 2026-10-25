from flask import Blueprint, request, jsonify

game_bp = Blueprint(
    "game",
    __name__,
    url_prefix="/api/game"
)

# Tạo phòng chơi
@game_bp.route("/rooms", methods=["POST"])
def create_room():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body không hợp lệ"
        }), 400

    username = data.get("username", "").strip()
    if not username:
        return jsonify({
            "success": False,
            "message": "Username không được để trống"
        }), 400

    # TODO: logic tạo phòng (lưu vào DB, tạo room_code...)
    return jsonify({
        "success": True,
        "message": "Tạo phòng thành công"
    }), 201

# Tham gia phòng
@game_bp.route("/rooms/<int:room_id>", methods=["POST"])
def join_room(room_id):
    # TODO: logic tham gia phòng
    return jsonify({
        "success": True,
        "message": f"Đã tham gia phòng {room_id}"
    }), 200

# Gửi nước đi
@game_bp.route("/moves/<int:room_id>", methods=["POST"])
def make_move(room_id):
    # TODO: logic xử lý nước đi
    return jsonify({
        "success": True,
        "message": f"Nước đi đã được gửi vào phòng {room_id}"
    }), 200

# Lấy trạng thái ván chơi
@game_bp.route("/state/<int:room_id>", methods=["GET"])
def get_state(room_id):
    # TODO: logic trả về trạng thái ván chơi
    return jsonify({
        "success": True,
        "message": f"Trạng thái phòng {room_id}"
    }), 200
