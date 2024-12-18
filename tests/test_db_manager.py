import unittest
from scripts.db_manager import initialize_db, add_book, list_books

class TestDBManager(unittest.TestCase):
    def test_add_book(self):
        initialize_db()
        add_book("Test Title", "Test Author", "Fiction", 2020, "1234567890", 4.5, "Read")
        books = list_books()
        self.assertTrue(len(books) > 0)

if __name__ == "__main__":
    unittest.main()
