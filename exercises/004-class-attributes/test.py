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


def get_car_class():
    app = load_app()
    assert hasattr(app, "Car"), "Create a class called Car in app.py"
    return app.Car


@pytest.mark.it("Car should have a class attribute wheels equal to 4")
def test_class_attribute():
    Car = get_car_class()
    assert "wheels" in Car.__dict__, "Define wheels directly in the class body, not inside __init__"
    assert Car.wheels == 4, "wheels should be 4"


@pytest.mark.it("Car should store brand and model as instance attributes")
def test_instance_attributes():
    car = get_car_class()("Ford", "Focus")
    assert car.brand == "Ford" and car.model == "Focus"
    assert "wheels" not in vars(car), "wheels should belong to the class, not to each instance"


@pytest.mark.it("description() should return '<brand> <model> with <wheels> wheels'")
def test_description():
    car = get_car_class()("Toyota", "Corolla")
    assert car.description() == "Toyota Corolla with 4 wheels"


@pytest.mark.it("description() should read wheels from the class attribute")
def test_description_uses_class_attribute():
    Car = get_car_class()
    Car.wheels = 6
    assert Car("Volvo", "FH").description() == "Volvo FH with 6 wheels", "Use self.wheels or Car.wheels instead of writing 4"
