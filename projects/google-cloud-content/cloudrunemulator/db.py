import sqlite3
from sqlite3 import Error

DATABASE_name = 'todo.db'


def get_conn():
    try:
        conn = sqlite3.connect(DATABASE_name)
        return conn
    except Error as e:
        print(e)


def create_table():
    tables = [
        """
        CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL, status TEXT NOT NULL)
        """
    ]
    db = get_conn()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def get_tables():
    cursor = get_conn().cursor()
    sql = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(sql)
    names = [row[0] for row in cursor.fetchall()]
    return names


def is_table(name):
    """Determine if a table exists"""
    return name in get_tables()
