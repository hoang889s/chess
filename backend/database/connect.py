import pymysql
from config import Config
print("PyMySQL:", pymysql.__version__)

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
