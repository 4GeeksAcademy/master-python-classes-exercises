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


def new_formatter():
    app = load_app()
    assert hasattr(app, "TextFormatter"), "Create a class called TextFormatter in app.py"
    return app.TextFormatter()


@pytest.mark.it("A new TextFormatter should start with an empty text")
def test_initial_text():
    formatter = new_formatter()
    assert formatter.text == "", "In __init__, set self.text to an empty string"


@pytest.mark.it("set_text() should save the text in the attribute text")
def test_set_text():
    formatter = new_formatter()
    formatter.set_text("hello")
    assert formatter.text == "hello", "set_text should store the value in self.text"


@pytest.mark.it("get_uppercase() should return the saved text in uppercase")
def test_get_uppercase():
    formatter = new_formatter()
    formatter.set_text("hello world")
    assert formatter.get_uppercase() == "HELLO WORLD"
    formatter.set_text("Python")
    assert formatter.get_uppercase() == "PYTHON", "get_uppercase should use the latest text"
