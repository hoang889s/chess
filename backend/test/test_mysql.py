import pymysql

print("PyMySQL:", pymysql.__version__)

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Hoang%145236",
    )

    print("Kết nối thành công!")

    with conn.cursor() as cur:
        cur.execute("SELECT VERSION()")
        print(cur.fetchone())

    conn.close()

except Exception as e:
    print(type(e))
    print(e)