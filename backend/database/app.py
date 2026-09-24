import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from database.connect import Connect
from database.create_db import Create_database
from database.create_all_table import DatabaseTableCreator
from database.config import Config
from database.extensions import db,jwt
from routes.auth import auth_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
jwt.init_app(app)
app.register_blueprint(auth_bp)
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