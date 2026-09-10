class Room:
    def __init__(self,id,room_code,owner_id,game_id,room_status,lock,created_at,updated_at):
        self.id = id
        self.room_code = room_code
        self.owner_id = owner_id
        self.game_id = game_id
        self.room_status = room_status
        self.lock = lock
        self.created_at = created_at
        self.updated_at = updated_at
    def test_room_print(self):
        print(f"ID phong: {self.id}")
        print(f"Ma phong: {self.room_code}")
        print(f"ID chu phong: {self.owner_id}")
        print(f"ID game: {self.game_id}")
        print(f"Trang thai phong: {self.room_status}")
        print(f"Phong bi khoa: {self.lock}")
        print(f"Thoi gian tao phong: {self.created_at}")
        print(f"Thoi gian cap nhat phong: {self.updated_at}")
    def return_value_room(self):
        return f"{self.id}+{self.room_code}+{self.owner_id}+{self.game_id}+{self.room_status}+{self.lock}+{self.created_at}+{self.updated_at}"
    