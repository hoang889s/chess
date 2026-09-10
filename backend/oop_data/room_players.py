class Room_players:
    def __init__(self,id,room_id,user_id,color,joined_at,left_at,status):
        self.id = id
        self.room_id = room_id
        self.user_id = user_id
        self.color = color
        self.joined_at = joined_at
        self.left_at = left_at
        self.status = status
    def test_room_players_print(self):
        print(f"ID người chơi: {self.id}")
        print(f"ID phòng: {self.room_id}")
        print(f"ID người dùng: {self.user_id}")
        print(f"Màu quân cờ: {self.color}")
        print(f"Thời gian tham gia: {self.joined_at}")
        print(f"Thời gian rời phòng: {self.left_at}")
        print(f"Trạng thái người chơi: {self.status}")
    def return_value_room_players(self):
        return f"{self.id}+{self.room_id}+{self.user_id}+{self.color}+{self.joined_at}+{self.left_at}+{self.status}"