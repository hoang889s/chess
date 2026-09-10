class Room_viewers:
    def __init__(self,id,room_id,user_id,joined_at,left_at):
        self.id = id
        self.room_id = room_id
        self.user_id = user_id
        self.joined_at = joined_at
        self.left_at = left_at
    def test_room_viewers_print(self):
        print(f"ID người xem: {self.id}")
        print(f"ID phòng: {self.room_id}")
        print(f"ID người dùng: {self.user_id}")
        print(f"Thời gian tham gia: {self.joined_at}")
        print(f"Thời gian rời phòng: {self.left_at}")
    def return_value_room_viewers(self):
        return f"{self.id}+{self.room_id}+{self.user_id}+{self.joined_at}+{self.left_at}"
    