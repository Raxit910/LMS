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

    # Tests for Borrowing Books
    def test_borrow_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.assertTrue(book.is_borrowed)

    def test_borrow_unavailable_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        with self.assertRaises(ValueError):
            self.library.borrow_book(book.isbn)  # Borrowing again should raise an error

    # Tests for Returning Books
    def test_return_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.library.return_book(book.isbn)
        self.assertFalse(book.is_borrowed)

    def test_return_unborrowed_book(self):
        book = Book(isbn="1234567890", title="The Guide", author="RK Narayan", year=1958)
        self.library.add_book(book)
        with self.assertRaises(ValueError):
            self.library.return_book(book.isbn)  # Returning an unborrowed book should raise an error

if __name__ == "__main__":
    unittest.main()
