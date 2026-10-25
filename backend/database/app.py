import sys
import os
BACKEND_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BACKEND_ROOT)

# Thư mục build frontend: backend/../frontend/chess_ui/dist
FRONTEND_DIST = os.path.abspath(os.path.join(BACKEND_ROOT, '..', 'frontend', 'chess_ui', 'dist'))

from flask import Flask, jsonify
from database.connect import Connect
from database.create_db import Create_database
from database.create_all_table import DatabaseTableCreator
from database.config import Config
from database.extensions import db,jwt
from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.game_bp import game_bp
from utils.jwt import  is_token_revokes

app = Flask(
    __name__,
    static_folder=FRONTEND_DIST,
    static_url_path=''
)

app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = Config.JWT_ACCESS_TOKEN_EXPIRES

db.init_app(app)
jwt.init_app(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header,jwt_payload):
    return is_token_revokes(jwt_payload)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(game_bp)

# Catch-all route: phục vụ index.html cho các đường dẫn frontend (/, /game, /login...)
# phải đăng ký SAU tất cả API routes để không ảnh hưởng đến API
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path.startswith('api/'):
        # API route không tồn tại -> trả về JSON 404 rõ ràng
        return jsonify({
            "success": False,
            "message": "Endpoint không tồn tại"
        }), 404
    from flask import send_from_directory
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    connect = None
    # tao ket noi voi database
    conn = Connect(connect)
    conn.connect_to_db()
    conn.show_pymysql()
    #tao database chess_web
    create = None
    cr = Create_database(create)
    cr.Cr_db()
    # tao ra table 
    table_creator = DatabaseTableCreator(app)
    table_creator.create_all_tables()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )