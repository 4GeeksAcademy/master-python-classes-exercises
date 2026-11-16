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


def get_classes():
    app = load_app()
    assert hasattr(app, "CollegeStudent"), "Create a class called CollegeStudent in app.py"
    return app.Student, app.CollegeStudent


@pytest.mark.it("CollegeStudent should inherit from Student")
def test_inherits():
    Student, CollegeStudent = get_classes()
    assert issubclass(CollegeStudent, Student), "Write class CollegeStudent(Student):"


@pytest.mark.it("CollegeStudent should have name, age, grade and major")
def test_attributes():
    _, CollegeStudent = get_classes()
    student = CollegeStudent("Alice", 20, 90, "Computer Science")
    assert (student.name, student.age, student.grade) == ("Alice", 20, 90), "Call super().__init__(name, age, grade)"
    assert student.major == "Computer Science", "Store the major in self.major"


@pytest.mark.it("You should use super() in CollegeStudent")
def test_uses_super():
    with open(APP_PATH, encoding="utf-8") as fh:
        assert "super()" in fh.read(), "Use super().__init__(...) to reuse the parent's __init__"


@pytest.mark.it("introduce() should be overridden with the new message")
def test_introduce():
    _, CollegeStudent = get_classes()
    student = CollegeStudent("Alice", 20, 90, "Computer Science")
    assert student.introduce() == "Hi there! I'm Alice, a college student majoring in Computer Science."


@pytest.mark.it("attend_lecture() should return the expected message")
def test_attend_lecture():
    _, CollegeStudent = get_classes()
    student = CollegeStudent("Bob", 22, 80, "Biology")
    assert student.attend_lecture() == "Bob is attending a lecture for Biology students."


@pytest.mark.it("study() should still work because it's inherited")
def test_study_inherited():
    _, CollegeStudent = get_classes()
    assert CollegeStudent("Bob", 22, 80, "Biology").study(2) == "Bob is studying for 2 hours."
