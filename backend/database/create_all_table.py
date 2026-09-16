from flask import Flask

from extensions import db

# Import tất cả models
import create_table.create_table_games 
import create_table.create_table_moves
import create_table.create_table_rooms
import create_table.create_table_room_players
import create_table.create_table_users
import create_table.create_table_views


class DatabaseTableCreator:

    def __init__(self, app: Flask):
        self.app = app

    def create_all_tables(self):
        with self.app.app_context():
            db.create_all()

            print("Tạo tất cả bảng thành công!")