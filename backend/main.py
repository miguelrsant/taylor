from flask import Flask
from flask_cors import CORS
from db.databese import execute_query
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

version = execute_query("SHOW server_version;")

max_connections = execute_query("SHOW max_connections;")


def count_connections_to_maindb():
    query = "SELECT count(*)::int FROM pg_stat_activity WHERE datname = %s;"

    db_name = os.getenv("POSTGRES_DB")
    params = (db_name,)
    connection_count = execute_query(query, params=params, fetch_results=True)
    return connection_count if connection_count is not None else 0


count = count_connections_to_maindb()


@app.get("/")
def index():
    return {
        "db": {
            "version": version,
            "max_connections": max_connections,
            "opened_connections": count
        }
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
