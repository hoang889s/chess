import os
from dotenv import load_dotenv
from sqlalchemy import URL
load_dotenv()
class Config:
    MYSQL_HOST=os.getenv("MYSQL_HOST")
    MYSQL_PORT=os.getenv("MYSQL_PORT")
    MYSQL_USER=os.getenv("MYSQL_USER")
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE=os.getenv("MYSQL_DATABASE")
    SQLALCHEMY_DATABASE_URI = URL.create(
        drivername="mysql+pymysql",
        username=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        database=MYSQL_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False