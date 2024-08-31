import unittest
from library import Library, Book

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    # Add Test case to add book
    def test_add_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        self.assertIn(book, self.library.books)
    
    # Additional test cases for edge conditions
    def test_add_duplicate_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        with self.assertRaises(ValueError):
            self.library.add_book(book)  # Adding the same book again should raise an error

if __name__ == "__main__":
    unittest.main()
