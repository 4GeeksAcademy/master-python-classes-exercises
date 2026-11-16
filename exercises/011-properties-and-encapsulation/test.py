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
    assert hasattr(app, "BankAccount"), "Create a class called BankAccount in app.py"
    return app.BankAccount


@pytest.mark.it("BankAccount should store the owner and start with balance 0 by default")
def test_init():
    BankAccount = get_class()
    account = BankAccount("Ana")
    assert account.owner == "Ana"
    assert account.balance == 0, "The default balance should be 0"
    assert BankAccount("Leo", 100).balance == 100


@pytest.mark.it("balance should be a read-only property")
def test_property():
    BankAccount = get_class()
    assert isinstance(BankAccount.__dict__.get("balance"), property), "Use @property to define balance"
    account = BankAccount("Ana", 100)
    with pytest.raises(AttributeError):
        account.balance = 999


@pytest.mark.it("deposit() and withdraw() should update the balance")
def test_operations():
    account = get_class()("Ana", 100)
    account.deposit(50)
    assert account.balance == 150, "deposit should add the amount"
    account.withdraw(30)
    assert account.balance == 120, "withdraw should subtract the amount"


@pytest.mark.it("deposit() should raise ValueError for amounts less than or equal to 0")
def test_invalid_deposit():
    account = get_class()("Ana", 100)
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.deposit(-10)
    assert account.balance == 100, "An invalid deposit should not change the balance"


@pytest.mark.it("withdraw() should raise ValueError for invalid amounts or insufficient funds")
def test_invalid_withdraw():
    account = get_class()("Ana", 100)
    with pytest.raises(ValueError):
        account.withdraw(500)
    with pytest.raises(ValueError):
        account.withdraw(-1)
    assert account.balance == 100, "An invalid withdrawal should not change the balance"
