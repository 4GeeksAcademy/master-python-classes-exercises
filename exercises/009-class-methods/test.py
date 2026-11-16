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
    assert hasattr(app, "CircleCalculator"), "Create a class called CircleCalculator in app.py"
    return app.CircleCalculator


@pytest.mark.it("CircleCalculator should have a class attribute pi equal to 3.14159")
def test_pi():
    CircleCalculator = get_class()
    assert "pi" in CircleCalculator.__dict__, "Define pi directly in the class body"
    assert CircleCalculator.pi == 3.14159


@pytest.mark.it("calculate_area should be a class method")
def test_is_classmethod():
    CircleCalculator = get_class()
    assert isinstance(CircleCalculator.__dict__.get("calculate_area"), classmethod), "Use the @classmethod decorator"


@pytest.mark.it("CircleCalculator.calculate_area(5) should return 78.53975")
def test_area():
    assert get_class().calculate_area(5) == pytest.approx(78.53975)


@pytest.mark.it("calculate_area should read pi from cls")
def test_uses_cls():
    CircleCalculator = get_class()
    CircleCalculator.pi = 3
    assert CircleCalculator.calculate_area(2) == 12, "Use cls.pi instead of writing the number"
