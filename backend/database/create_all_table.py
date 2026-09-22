from flask import Flask

from .extensions import db

# Import tất cả models
from .create_table import create_table_games
from .create_table import create_table_moves
from .create_table import create_table_rooms
from .create_table import create_table_room_players
from .create_table import create_table_users
from .create_table import create_table_views


class DatabaseTableCreator:

    def __init__(self, app: Flask):
        self.app = app

    def create_all_tables(self):
        with self.app.app_context():
            db.create_all()

            print("Tạo tất cả bảng thành công!")