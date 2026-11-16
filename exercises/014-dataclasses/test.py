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


from dataclasses import fields, is_dataclass


def get_class():
    app = load_app()
    assert hasattr(app, "Product"), "Create a class called Product in app.py"
    return app.Product


@pytest.mark.it("Product should be a dataclass with the fields name, price and quantity")
def test_is_dataclass():
    Product = get_class()
    assert is_dataclass(Product), "Use the @dataclass decorator"
    assert [f.name for f in fields(Product)] == ["name", "price", "quantity"], "Declare the fields in this order: name, price, quantity"


@pytest.mark.it("quantity should be 0 by default")
def test_default_quantity():
    assert get_class()("Mouse", 20.0).quantity == 0


@pytest.mark.it("The dataclass should generate __repr__ and __eq__")
def test_generated_methods():
    Product = get_class()
    assert repr(Product("Mouse", 20.0, 1)) == "Product(name='Mouse', price=20.0, quantity=1)"
    assert Product("Mouse", 20.0, 1) == Product("Mouse", 20.0, 1)


@pytest.mark.it("total_value() should return price * quantity")
def test_total_value():
    Product = get_class()
    assert Product("Laptop", 999.99, 2).total_value() == pytest.approx(1999.98)
    assert Product("Mouse", 20.0).total_value() == 0
