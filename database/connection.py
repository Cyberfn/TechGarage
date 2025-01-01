import mariadb
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        conn = mariadb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME")
        )
        print("Conexão bem-sucedida!")
        return conn
    except mariadb.Error as e:
        print(f"Erro: {e}")
        return None

conectar()