from flask import Blueprint, request, jsonify
from database.extensions import db
from utils.validator import validate_username, validate_email, validate_password

game_bp = Blueprint(
    "game",
    __name__,
    url_prefix="/api/game"
)

# Create a room
@game_bp.route("/rooms", methods=["POST"])
def create_room():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "message": "Request body không hợp lệ"}), 400
    
    username = data.get("username", "").strip()
    if not username:
        return jsonify({"success": False, "message": "Username không được để trống"}), 400
    
    # Create room logic would go here
    return jsonify({"success": True, "message": "Room created successfully"}), 201

# Join a room
@game_bp.route("/rooms/<int:room_id>", methods=["POST"])
def join_room(room_id):
    # Implementation would go here
    return jsonify({"success": True, "message": f"Joined room {room_id}"}), 200

# Make a move
@game_bp.route("/moves/<int:room_id>", methods=["POST"])
def make_move(room_id):
    # Implementation would go here
    return jsonify({"success": True, "message": f"Move made in room {room_id}"}), 200

# Get game state
@game_bp.route("/state/<int:room_id>", methods=["GET"])
def get_state(room_id):
    # Implementation would go here
    return jsonify({"success": True, "message": f"State of room {room_id}"}), 200
