Certainly! Here are new titles, authors, and ISBNs for both books:

```python
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"'{book.title}', written by: '{book.author}', ISBN: {book.isbn}")

# New books and authors
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780241950425")
book2 = Book("The Hobbit", "J.R.R. Tolkien", "9780261102217")

library = Library()
library.add_book(book1)
library.add_book(book2)
print("------------------------")
library.display_books()
print("------------------------")
library.remove_book("9780241950425")
print("------------------------")
library.display_books()
```

Now, the first book is "The Catcher in the Rye" by J.D. Salinger, and the second book is "The Hobbit" by J.R.R. Tolkien.