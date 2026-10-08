"""Kleine Bibliotheksverwaltung mit SQLite und einer n:m-Beziehung."""

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


def get_lends(connection: sqlite3.Connection, book_id: int) -> list[tuple[str, str]]:
    """Gib (Kundenname, Ausleihdatum) fuer ein Buch chronologisch zurueck."""
    cursor = connection.execute("""
        SELECT customers.name, lends.lend_date
        FROM lends
        JOIN customers ON customers.id = lends.customer_id
        JOIN books ON books.id = lends.book_id
        WHERE books.id = ?
        ORDER BY lends.lend_date, lends.id
    """, (book_id,))
    return cursor.fetchall()


if __name__ == "__main__":
    connection = create_database()
    try:
        with connection:
            connection.executemany(
                "INSERT INTO books (id, title) VALUES (?, ?)",
                [(1, "Python lernen"), (2, "Roboter bauen")],
            )
            connection.executemany(
                "INSERT INTO customers (id, name) VALUES (?, ?)",
                [(1, "Anna"), (2, "Ben")],
            )
            connection.executemany(
                "INSERT INTO lends (book_id, customer_id, lend_date) VALUES (?, ?, ?)",
                [(1, 1, "2026-09-01"), (1, 2, "2026-09-15"),
                 (2, 1, "2026-09-20"), (1, 1, "2026-10-01")],
            )
        print(get_lends(connection, 1))
    finally:
        connection.close()
