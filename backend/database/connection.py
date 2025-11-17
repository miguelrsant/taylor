import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/app/.env")

DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def execute_query(query, params=None, fetch_results=True):
    conn = get_connection()
    if conn is None:
        return None

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query, params)

                if fetch_results:
                    result_list = cur.fetchall()
                    if result_list and isinstance(result_list, list) and len(result_list) > 0:
                        return result_list[0][0]
                    else:
                        return None

                return True

    except psycopg2.Error as e:
        print(f"Erro durante a execução da query: {e}")
        return False

    finally:
        if conn:
            conn.close()
