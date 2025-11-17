import os
from database.connection import execute_query


def get_version():
    return execute_query("SHOW server_version;")


def get_max_connections():
    return execute_query("SHOW max_connections;")


def count_connections_to_maindb():
    query = "SELECT count(*)::int FROM pg_stat_activity WHERE datname = %s;"
    db_name = os.getenv("POSTGRES_DB")
    params = (db_name,)
    result = execute_query(query, params=params, fetch_results=True)
    return result if result is not None else 0
