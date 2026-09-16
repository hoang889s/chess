from flask import Flask
from connect import Connect
from create_db import Create_database
from create_all_table import DatabaseTableCreator
from config import Config
from extensions import db
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)
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

