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


import inspect


def get_class():
    app = load_app()
    assert hasattr(app, "DivisibleBySeven"), "Create a class called DivisibleBySeven in app.py"
    return app.DivisibleBySeven


@pytest.mark.it("generate() should be a generator (use yield)")
def test_is_generator():
    DivisibleBySeven = get_class()
    assert inspect.isgeneratorfunction(DivisibleBySeven.generate), "Use yield inside generate()"


@pytest.mark.it("DivisibleBySeven(30).generate() should produce 0, 7, 14, 21, 28")
def test_values():
    assert list(get_class()(30).generate()) == [0, 7, 14, 21, 28]


@pytest.mark.it("The upper limit n should be included")
def test_inclusive():
    assert list(get_class()(14).generate()) == [0, 7, 14]
    assert list(get_class()(6).generate()) == [0]
