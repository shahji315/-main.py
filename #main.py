# main.py
from book import Book 
from library import Library

# Create some book objects
book1 = Book("Python Programming", "John Smith")
book2 = Book ("Data Science Essentials""Alice Johnson")
book3 = Book("Web Development Basics""Bob Wilson")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2) 
library.add_book(book3)

# Borrow and return books
print(library.borrow_book("Python Programming")) # Borrow book1
print(library.borrow_book("Python Programming")) # Already borrowed 
print(library.return_book("Python Programming")) # Return booki
print(library.return_book("Python Programming"))# Not currently borrowed

# Count how many books are currently borrowed
print (f"Number of borrowed books: {library.borrowed_count}")
