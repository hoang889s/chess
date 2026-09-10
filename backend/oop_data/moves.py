class Move:
    def __init__(self,id,game_id,player_id,move_number,move,promotion,san,fen,created_at):
        self.id = id
        self.game_id = game_id
        self.player_id = player_id
        self.move_number = move_number
        self.move = move
        self.promotion = promotion
        self.san = san
        self.fen = fen
        self.created_at = created_at
    def test_move_print(self):
        print(f"ID nước đi: {self.id}")
        print(f"ID game: {self.game_id}")
        print(f"ID người chơi: {self.player_id}")
        print(f"Số nước đi: {self.move_number}")
        print(f"Nước đi: {self.move}")
        print(f"Quân cờ được thăng cấp: {self.promotion}")
        print(f"San: {self.san}")
        print(f"FEN hiện tại: {self.fen}")
        print(f"Thời gian tạo nước đi: {self.created_at}")
    def return_value_move(self):
        return f"{self.id}+{self.game_id}+{self.player_id}+{self.move_number}+{self.move}+{self.promotion}+{self.san}+{self.fen}+{self.created_at}"