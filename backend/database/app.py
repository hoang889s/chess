from connect import Connect
from create_db import Create_database
if __name__ == "__main__":
    connect = None
    # tao ket noi voi database
    conn = Connect(connect)
    conn.connect_to_db()
    conn.show_pymysql()
    #tao database chess_web
    create = None
    cr = Create_database(create)
    cr.Cr_db()
