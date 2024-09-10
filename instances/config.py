import os
from dotenv import load_dotenv #Para cargar variables de entorno desde un archivo a python

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")
    SECRET_KEY = os.getenv("HEX_SEC_KEY")
