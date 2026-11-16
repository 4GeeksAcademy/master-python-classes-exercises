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


def get_pet_class():
    app = load_app()
    assert hasattr(app, "Pet"), "Create a class called Pet in app.py"
    return app.Pet


@pytest.mark.it("The class Pet should exist")
def test_class_exists():
    get_pet_class()


@pytest.mark.it("Pet should store name, species and age as attributes")
def test_attributes():
    pet = get_pet_class()("Rocky", "dog", 5)
    assert pet.name == "Rocky", "Store the name in self.name"
    assert pet.species == "dog", "Store the species in self.species"
    assert pet.age == 5, "Store the age in self.age"


@pytest.mark.it("describe() should return '<name> is a <age> year old <species>.'")
def test_describe():
    pet = get_pet_class()("Luna", "cat", 3)
    result = pet.describe()
    assert result == "Luna is a 3 year old cat.", f"Expected 'Luna is a 3 year old cat.' but got {result!r}"


@pytest.mark.it("birthday() should increase the age by 1 and return it")
def test_birthday():
    pet = get_pet_class()("Luna", "cat", 3)
    assert pet.birthday() == 4, "birthday() should return the new age"
    assert pet.age == 4, "birthday() should update self.age"
    assert pet.describe() == "Luna is a 4 year old cat.", "describe() should use the updated age"
