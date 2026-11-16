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


from dataclasses import is_dataclass


def get_app():
    app = load_app()
    for name in ["CartItem", "ShoppingCart"]:
        assert hasattr(app, name), f"Create {name} in app.py"
    return app


def filled_cart(app=None):
    app = app or get_app()
    cart = app.ShoppingCart()
    cart.add_item("apple", 0.5, 4)
    cart.add_item("bread", 2.25)
    cart.add_item("apple", 0.5, 2)
    return cart


@pytest.mark.it("CartItem should be a dataclass with quantity 1 by default and a subtotal() method")
def test_cart_item():
    CartItem = get_app().CartItem
    assert is_dataclass(CartItem), "Use @dataclass on CartItem"
    item = CartItem("milk", 1.5)
    assert item.quantity == 1, "quantity should default to 1"
    assert CartItem("milk", 1.5, 3).subtotal() == pytest.approx(4.5)


@pytest.mark.it("add_item() should add new products and increase the quantity of existing ones")
def test_add_item():
    app = get_app()
    cart = filled_cart(app)
    assert set(cart.items) == {"apple", "bread"}, "items should be a dict with the product names as keys"
    assert isinstance(cart.items["apple"], app.CartItem), "The values of items should be CartItem objects"
    assert cart.items["apple"].quantity == 6, "Adding an existing product should increase its quantity"
    assert cart.items["bread"].quantity == 1, "The default quantity should be 1"


@pytest.mark.it("total() should return the sum of the subtotals rounded to 2 decimals")
def test_total():
    cart = filled_cart()
    assert cart.total() == 5.25
    assert get_app().ShoppingCart().total() == 0


@pytest.mark.it("len(cart) should return the total number of units")
def test_len():
    assert len(filled_cart()) == 7


@pytest.mark.it("remove_item() should remove a product and raise KeyError if it doesn't exist")
def test_remove_item():
    cart = filled_cart()
    cart.remove_item("bread")
    assert "bread" not in cart.items
    assert cart.total() == 3.0
    with pytest.raises(KeyError):
        cart.remove_item("chocolate")
