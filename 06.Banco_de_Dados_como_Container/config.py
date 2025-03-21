import os

from dotenv import load_dotenv


load_dotenv()
db_user = os.getenv("db_user")
db_host = os.getenv("db_host")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")