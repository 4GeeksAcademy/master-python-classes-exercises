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


def get_point_class():
    app = load_app()
    assert hasattr(app, "Point"), "Create a class called Point in app.py"
    return app.Point


@pytest.mark.it("Point should store x and y")
def test_attributes():
    point = get_point_class()(3, 4)
    assert point.x == 3 and point.y == 4


@pytest.mark.it("repr(Point(1, 2)) should be 'Point(1, 2)'")
def test_repr():
    Point = get_point_class()
    assert repr(Point(1, 2)) == "Point(1, 2)", f"Got {repr(Point(1, 2))!r}"
    assert repr([Point(0, 0)]) == "[Point(0, 0)]", "__repr__ is also used when the point is inside a list"


@pytest.mark.it("Two points with the same coordinates should be equal")
def test_equal():
    Point = get_point_class()
    assert Point(1, 2) == Point(1, 2)


@pytest.mark.it("Points with different coordinates, or other types, should not be equal")
def test_not_equal():
    Point = get_point_class()
    assert Point(1, 2) != Point(2, 1)
    assert (Point(1, 2) == "Point(1, 2)") is False, "Comparing with a non-Point should return False"
