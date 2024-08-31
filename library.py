#Implement add book feature
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    # Implement Adding Books
    def add_book(self, book):
        if book in self.books:
            raise ValueError("Book already exists in the library.")
        self.books.append(book)

    # Implement Borrowing Books
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    raise ValueError("Book is already borrowed.")
                book.is_borrowed = True
                return
        raise ValueError("Book not found in the library.")
    
    # Implement Returning Books
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise ValueError("Book is not borrowed.")
                book.is_borrowed = False
                return
        raise ValueError("Book not found in the library.")
    
    # Implement Viewing Available Books
    def view_available_books(self):
        return [book for book in self.books if not book.is_borrowed]
