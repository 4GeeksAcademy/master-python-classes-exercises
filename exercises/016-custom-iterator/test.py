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
    assert hasattr(app, "Countdown"), "Create a class called Countdown in app.py"
    return app.Countdown


@pytest.mark.it("Countdown should implement __iter__ and __next__")
def test_protocol():
    Countdown = get_class()
    assert hasattr(Countdown, "__iter__") and hasattr(Countdown, "__next__"), "Implement both __iter__ and __next__"
    countdown = Countdown(2)
    assert iter(countdown) is countdown, "__iter__ should return self"


@pytest.mark.it("list(Countdown(5)) should be [5, 4, 3, 2, 1]")
def test_values():
    assert list(get_class()(5)) == [5, 4, 3, 2, 1]


@pytest.mark.it("__next__ should raise StopIteration at the end")
def test_stop_iteration():
    countdown = get_class()(1)
    assert next(countdown) == 1
    with pytest.raises(StopIteration):
        next(countdown)
