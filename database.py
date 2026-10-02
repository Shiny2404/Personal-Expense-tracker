import sqlite3
import os


DATABASE_FOLDER = "data"
DATABASE_NAME = "expenses.db"
DATABASE_PATH = os.path.join(DATABASE_FOLDER, DATABASE_NAME)


def create_database():
    """
    Creates the data folder and expenses table
    if they do not already exist.
    """

    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def get_connection():
    """
    Returns a connection to the SQLite database.
    """

    return sqlite3.connect(DATABASE_PATH)