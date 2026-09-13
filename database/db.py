import sqlite3
from pathlib import Path


DB_PATH = Path("database/travel_concierge.db")


def get_connection():
    """
    Create and return a SQLite database connection.
    """
    return sqlite3.connect(DB_PATH)


def create_tables():
    """
    Create the search_history table if it does not exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            search_type TEXT NOT NULL,
            destination TEXT,
            check_in TEXT,
            check_out TEXT,
            adults INTEGER,
            query TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()


def save_search(
    search_type,
    destination=None,
    check_in=None,
    check_out=None,
    adults=None,
    query=None
):
    """
    Save a travel search into the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO search_history
        (
            search_type,
            destination,
            check_in,
            check_out,
            adults,
            query
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            search_type,
            destination,
            check_in,
            check_out,
            adults,
            query
        )
    )

    connection.commit()
    connection.close()


def get_search_history():
    """
    Return all saved searches.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM search_history
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows