# library_system.py

# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize the Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of the Book."""
        return f"'{self.title}' by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size  # in megabytes

    def __str__(self):
        """String representation of the EBook."""
        return f"'{self.title}' by {self.author} (EBook, {self.file_size}MB)"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of the PrintBook."""
        return f"'{self.title}' by {self.author} (Print, {self.page_count} pages)"


# Composition Class - Library
class Library:
    def __init__(self):
        """Initialize the Library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library with details."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

