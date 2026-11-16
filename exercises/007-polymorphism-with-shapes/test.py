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


import math


def get_app():
    app = load_app()
    for name in ["Rectangle", "Circle", "total_area"]:
        assert hasattr(app, name), f"Create {name} in app.py"
    return app


@pytest.mark.it("Rectangle and Circle should inherit from Shape")
def test_inheritance():
    app = get_app()
    assert issubclass(app.Rectangle, app.Shape), "Write class Rectangle(Shape):"
    assert issubclass(app.Circle, app.Shape), "Write class Circle(Shape):"


@pytest.mark.it("Rectangle(2, 3).area() should return 6")
def test_rectangle_area():
    assert get_app().Rectangle(2, 3).area() == 6


@pytest.mark.it("Circle(1).area() should return math.pi")
def test_circle_area():
    assert get_app().Circle(1).area() == pytest.approx(math.pi)


@pytest.mark.it("total_area() should add the areas of every shape, rounded to 2 decimals")
def test_total_area():
    app = get_app()
    assert app.total_area([app.Rectangle(2, 3), app.Circle(1), app.Rectangle(1, 1)]) == 10.14
    assert app.total_area([app.Circle(2)]) == 12.57
    assert app.total_area([]) == 0
