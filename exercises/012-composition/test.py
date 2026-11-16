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


def build_library():
    app = load_app()
    assert hasattr(app, "Library"), "Create a class called Library in app.py"
    library = app.Library()
    library.add_book(app.Book("1984", "George Orwell"))
    library.add_book(app.Book("Dune", "Frank Herbert"))
    library.add_book(app.Book("Animal Farm", "George Orwell"))
    return app, library


@pytest.mark.it("A new Library should start with an empty list of books")
def test_empty():
    app = load_app()
    assert hasattr(app, "Library"), "Create a class called Library in app.py"
    assert app.Library().books == [], "Create self.books = [] in __init__"


@pytest.mark.it("add_book() should store Book objects in books")
def test_add_book():
    app, library = build_library()
    assert len(library.books) == 3
    assert all(isinstance(book, app.Book) for book in library.books), "books should contain Book objects"


@pytest.mark.it("find_by_author() should return the titles of that author's books")
def test_find_by_author():
    _, library = build_library()
    assert library.find_by_author("George Orwell") == ["1984", "Animal Farm"]
    assert library.find_by_author("Unknown") == []


@pytest.mark.it("len(library) should return the number of books")
def test_len():
    _, library = build_library()
    assert len(library) == 3, "Implement the __len__ method"
