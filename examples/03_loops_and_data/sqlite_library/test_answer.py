"""Tests mit eigenen Bibliotheksdaten."""

import sqlite3
import unittest

import answer


class Checker(unittest.TestCase):
    def setUp(self):
        self.connection = answer.create_database()
        self.addCleanup(self.connection.close)
        with self.connection:
            self.connection.executemany(
                "INSERT INTO books (id, title) VALUES (?, ?)",
                [(10, "SQL entdecken"), (20, "SQL entdecken"), (30, "Mathematik")],
            )
            self.connection.executemany(
                "INSERT INTO customers (id, name) VALUES (?, ?)",
                [(5, "Clara"), (6, "David"), (7, "Clara")],
            )
            self.connection.executemany(
                "INSERT INTO lends (id, book_id, customer_id, lend_date) VALUES (?, ?, ?, ?)",
                [(1, 10, 5, "2025-03-20"), (2, 20, 5, "2025-01-01"),
                 (3, 10, 6, "2025-02-01"), (4, 10, 5, "2025-04-01"),
                 (5, 10, 7, "2025-04-01")],
            )

    def test_all_lends_for_specific_book_in_date_order(self):
        self.assertEqual(answer.get_lends(self.connection, 10), [
            ("David", "2025-02-01"),
            ("Clara", "2025-03-20"),
            ("Clara", "2025-04-01"),
            ("Clara", "2025-04-01"),
        ])

    def test_customer_can_borrow_multiple_books(self):
        self.assertEqual(answer.get_lends(self.connection, 20),
                         [("Clara", "2025-01-01")])

    def test_book_without_lends(self):
        self.assertEqual(answer.get_lends(self.connection, 30), [])

    def test_unknown_book(self):
        self.assertEqual(answer.get_lends(self.connection, 999), [])

    def test_foreign_keys_reject_unknown_book_or_customer(self):
        for book_id, customer_id in [(999, 5), (10, 999)]:
            with self.subTest(book_id=book_id, customer_id=customer_id):
                with self.assertRaises(sqlite3.IntegrityError):
                    self.connection.execute(
                        "INSERT INTO lends (book_id, customer_id, lend_date) VALUES (?, ?, ?)",
                        (book_id, customer_id, "2025-05-01"),
                    )


if __name__ == "__main__":
    unittest.main()
