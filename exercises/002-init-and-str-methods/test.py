import importlib.util
import os

import pytest

APP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")


def load_app():
    """Load the student's app.py as a fresh module."""
    spec = importlib.util.spec_from_file_location("student_app", APP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_book_class():
    app = load_app()
    assert hasattr(app, "Book"), "Create a class called Book in app.py"
    return app.Book


@pytest.mark.it("The class Book should store title, author and year")
def test_attributes():
    book = get_book_class()("Dune", "Frank Herbert", 1965)
    assert book.title == "Dune", "Store the title in self.title"
    assert book.author == "Frank Herbert", "Store the author in self.author"
    assert book.year == 1965, "Store the year in self.year"


@pytest.mark.it("Printing a Book should show its title, author and year in three lines")
def test_str():
    book = get_book_class()("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    expected = "Book Title: The Great Gatsby\nAuthor: F. Scott Fitzgerald\nYear: 1925"
    assert str(book) == expected, f"Expected:\n{expected}\n\nBut got:\n{str(book)}"


@pytest.mark.it("__str__ should work with any book")
def test_str_other_book():
    book = get_book_class()("Dune", "Frank Herbert", 1965)
    assert str(book) == "Book Title: Dune\nAuthor: Frank Herbert\nYear: 1965"
