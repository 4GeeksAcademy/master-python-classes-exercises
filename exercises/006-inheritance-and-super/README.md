# `006` Inheritance and `super()`

With **inheritance**, a child class receives all the attributes and methods of a parent class, and can add new ones or **override** existing ones.

```py
class HighSchoolStudent(Student):  # The parent class goes in parentheses
    def __init__(self, name, age, grade, specialization):
        super().__init__(name, age, grade)  # Reuse the parent's __init__
        self.specialization = specialization

    def study(self, hours):  # Override a parent method
        return f"{self.name} is studying {self.specialization} for {hours} hours."
```

`super()` gives you access to the parent class, so you don't repeat its code.

## 📝 Instructions:

1. In `app.py` you already have a `Student` class. Don't modify it.

2. Create a class `CollegeStudent` that inherits from `Student` and adds the attribute `major`. Use `super()` in its `__init__`.

3. Override `introduce()` so it **returns** `"Hi there! I'm <name>, a college student majoring in <major>."`

4. Add a new method `attend_lecture()` that **returns** `"<name> is attending a lecture for <major> students."`

## 📎 Example:

```py
alice = CollegeStudent("Alice", 20, 90, "Computer Science")
print(alice.introduce())  # Hi there! I'm Alice, a college student majoring in Computer Science.
print(alice.study(3))  # Alice is studying for 3 hours.  (inherited, not changed)
print(alice.attend_lecture())  # Alice is attending a lecture for Computer Science students.
```

## 💡 Hint:

+ Learn more about `super()` in [Real Python: Supercharge Your Classes With Python super()](https://realpython.com/python-super/).
