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
    assert hasattr(app, "Person"), "Create a class called Person in app.py"
    return app.Person


@pytest.mark.it("Person should store name and age")
def test_init():
    person = get_class()("Ana", 25)
    assert person.name == "Ana" and person.age == 25


@pytest.mark.it("from_string and from_birth_year should be class methods")
def test_are_classmethods():
    Person = get_class()
    for name in ["from_string", "from_birth_year"]:
        assert isinstance(Person.__dict__.get(name), classmethod), f"Use @classmethod on {name}"


@pytest.mark.it("Person.from_string('Ana,25') should return a Person named Ana aged 25")
def test_from_string():
    Person = get_class()
    person = Person.from_string("Ana,25")
    assert isinstance(person, Person), "from_string should return a Person instance"
    assert person.name == "Ana"
    assert person.age == 25, "The age must be converted to int"


@pytest.mark.it("Person.from_birth_year('Leo', 2000, 2026) should return a Person aged 26")
def test_from_birth_year():
    Person = get_class()
    person = Person.from_birth_year("Leo", 2000, 2026)
    assert isinstance(person, Person), "from_birth_year should return a Person instance"
    assert (person.name, person.age) == ("Leo", 26)


@pytest.mark.it("The constructors should use cls so they also work for child classes")
def test_uses_cls():
    Person = get_class()

    class Employee(Person):
        pass

    assert isinstance(Employee.from_string("Eva,30"), Employee), "Return cls(...) instead of Person(...)"
