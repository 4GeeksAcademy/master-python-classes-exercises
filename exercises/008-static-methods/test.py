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


def get_class():
    app = load_app()
    assert hasattr(app, "MathOperations"), "Create a class called MathOperations in app.py"
    return app.MathOperations


@pytest.mark.it("add_numbers and is_even should be static methods")
def test_are_static():
    MathOperations = get_class()
    for name in ["add_numbers", "is_even"]:
        assert name in MathOperations.__dict__, f"Define the method {name} inside MathOperations"
        assert isinstance(MathOperations.__dict__[name], staticmethod), f"Use the @staticmethod decorator on {name}"


@pytest.mark.it("MathOperations.add_numbers(10, 15) should return 25")
def test_add_numbers():
    MathOperations = get_class()
    assert MathOperations.add_numbers(10, 15) == 25
    assert MathOperations.add_numbers(-1, 1) == 0


@pytest.mark.it("MathOperations.is_even() should return True for even numbers and False for odd numbers")
def test_is_even():
    MathOperations = get_class()
    assert MathOperations.is_even(4) is True
    assert MathOperations.is_even(7) is False
    assert MathOperations.is_even(0) is True
