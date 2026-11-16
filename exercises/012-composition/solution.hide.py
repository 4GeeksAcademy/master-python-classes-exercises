class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [book.title for book in self.books if book.author == author]

    def __len__(self):
        return len(self.books)


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Dune", "Frank Herbert"))
library.add_book(Book("Animal Farm", "George Orwell"))
print(len(library))
print(library.find_by_author("George Orwell"))
