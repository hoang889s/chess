import pymysql
from config import Config

class Connect:
    def __init__(self,conn):
        self.conn = conn
    def connect_to_db(self):
        try:
            conn = pymysql.connect(
                host=Config.MYSQL_HOST,
                port=int(Config.MYSQL_PORT),
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
            )
            print("Kết nối thành công!")
            with conn.cursor() as cur: 
                cur.execute("SELECT VERSION()")
                print(cur.fetchone())
            conn.close()
        except Exception as e:
            print(type(e))
            print(e)
    def show_pymysql(self):
        print("PyMySQL:", pymysql.__version__)




