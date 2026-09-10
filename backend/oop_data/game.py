class Game:
    def __init__(self,id,white_player_id,black_Player_id,game_mode,ai_difficulty,game_status,game_result,turn,fen,pgn,start_time,end_time,created_at):
        self.id = id
        self.white_player_id = white_player_id
        self.black_Player_id = black_Player_id
        self.game_mode = game_mode
        self.ai_difficulty = ai_difficulty
        self.game_status = game_status
        self.game_result = game_result
        self.turn = turn
        self.fen = fen
        self.pgn = pgn
        self.start_time = start_time
        self.end_time = end_time
        self.created_at = created_at
    def test_game_print(self):
        print(f"ID game: {self.id}")
        print(f"ID nguoi choi quan trang: {self.white_player_id}")
        print(f"ID nguoi choi quan den: {self.black_Player_id}")
        print(f"Che do choi: {self.game_mode}")
        print(f"Muc do AI: {self.ai_difficulty}")
        print(f"Trang thai game: {self.game_status}")
        print(f"Kết quả game: {self.game_result}")
        print(f"Lượt đi hiện tại: {self.turn}")
        print(f"FEN hien tai: {self.fen}")
        print(f"PGN hien tai: {self.pgn}")
        print(f"Thoi gian bat dau game: {self.start_time}")
        print(f"Thoi gian ket thuc game: {self.end_time}")
        print(f"Thoi gian tao game: {self.created_at}")
    def return_value_game(self):
        return f"{self.id}+{self.white_player_id}+{self.black_Player_id}+{self.game_mode}+{self.ai_difficulty}+{self.game_status}+{self.game_result}+{self.turn}+{self.fen}+{self.pgn}+{self.start_time}+{self.end_time}+{self.created_at}"