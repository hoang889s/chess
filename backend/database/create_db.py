# tao ra database khi chua co ma co roi thi khong tao nua
from config import Config
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
# phải chuyển về dạng endcode để không hiểu sai ký pải chính xác là dạng mysql+pymysql://root:abc%40123@localhost:3306 ví dụ như thế nó sẽ không hiểu mật khẩu
DATABASE_URL = (
    f"mysql+pymysql://{Config.MYSQL_USER}:"
    f"{quote_plus(Config.MYSQL_PASSWORD)}"
    f"@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}"
)
class Create_database:
    def __init__(self,engine):
        self.engine = create_engine(
            DATABASE_URL
        )
    def Cr_db(self):
        with self.engine.connect() as conn:
            conn.execute(text(f"""
                CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DATABASE}
                CHARACTER SET utf8mb4
                COLLATE utf8mb4_unicode_ci;
            """))
            conn.commit()
        print("Tạo database thành công!")

