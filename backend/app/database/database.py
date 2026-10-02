import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "travel_history.db")


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

    connection = None

    try:
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
        return True

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False

    finally:
        if connection:
            connection.close()

def get_search_history():
    """
    Return all saved searches.
    """

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM search_history
            ORDER BY created_at DESC
            """
        )

        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return []

    finally:
        if connection:
            connection.close()