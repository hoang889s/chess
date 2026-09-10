class User:
    def __init__(self,id,username,password,email,level,role,status,win,lost,created_at,updated_at):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.level = level
        self.role = role
        self.status = status
        self.win = win
        self.lost = lost
        self.created_at = created_at
        self.updated_at = updated_at
    def test_user_print(self):
        print(f"ID nguoi dung: {self.id}")
        print(f"Ten nguoi dung: {self.username}")
        print(f"Mat khau: {self.password}")
        print(f"Email: {self.email}")
        print(f"Cap do: {self.level}")
        print(f"Vai tro: {self.role}")
        print(f"Trang thai: {self.status}")
        print(f"So tran thang: {self.win}")
        print(f"So tran thua: {self.lost}")
        print(f"Thoi gian tao tai khoan: {self.created_at}")
        print(f"Thoi gian cap nhat: {self.updated_at}")
    def return_value_user(self):
        return f"{self.id}+{self.username}+{self.password}+{self.email}+{self.level}+{self.role}+{self.status}+{self.win}+{self.lost}+{self.created_at}+{self.updated_at}"
        



