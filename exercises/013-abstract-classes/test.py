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


from abc import ABC


def get_app():
    app = load_app()
    for name in ["PaymentMethod", "CreditCard", "PayPal"]:
        assert hasattr(app, name), f"Create the class {name} in app.py"
    return app


@pytest.mark.it("PaymentMethod should be an abstract class that can't be instantiated")
def test_abstract():
    app = get_app()
    assert issubclass(app.PaymentMethod, ABC), "PaymentMethod should inherit from ABC"
    with pytest.raises(TypeError):
        app.PaymentMethod()


@pytest.mark.it("CreditCard and PayPal should inherit from PaymentMethod")
def test_inheritance():
    app = get_app()
    assert issubclass(app.CreditCard, app.PaymentMethod)
    assert issubclass(app.PayPal, app.PaymentMethod)


@pytest.mark.it("CreditCard.pay() should show the last 4 digits of the card")
def test_credit_card():
    card = get_app().CreditCard("4111222233334444")
    assert card.pay(50) == "Paid 50 with card ending in 4444"


@pytest.mark.it("PayPal.pay() should show the account email")
def test_paypal():
    paypal = get_app().PayPal("ana@example.com")
    assert paypal.pay(20) == "Paid 20 with PayPal account ana@example.com"
