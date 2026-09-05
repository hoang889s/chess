class User:
    def __init__(self,id,username,password,level,status,win,lost,email):
        self.id = id
        self.username = username
        # hay luu y pass vi no can duoc bao mat truoc khi dua tren server
        self.password = password
        self.level = level
        self.status = True
        self.win = win
        self.lost = lost
        self.email = email
    def test_user_print(self):
        print(f"Id người dùng: {self.id}")
        print(f"Mật khẩu người dùng: {self.password}")
        print(f"Trình độ: {self.level}")
        print(f"Trạng thái: {self.status}")
        print(f"Số trận thắng: {self.win}")
        print(f"Số trận thua: {self.lost}")
        print(f"Email: {self.email}")
    def return_value_user(self):
        return f"{self.id}+{self.username}+{self.password}+{self.level}+{self.status}+{self.win}+{self.lost}+{self.email}"

        

        



