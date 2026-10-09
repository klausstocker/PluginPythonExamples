import sqlite3

def create_database() -> sqlite3.Connection:
    """Erstelle eine leere Datenbank im Arbeitsspeicher."""
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL
        );
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        CREATE TABLE lends (
            id INTEGER PRIMARY KEY,
            book_id INTEGER NOT NULL REFERENCES books(id),
            customer_id INTEGER NOT NULL REFERENCES customers(id),
            lend_date TEXT NOT NULL
        );
    """)
    return connection