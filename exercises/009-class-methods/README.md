# `009` Class Methods

A **class method** receives the class itself as its first parameter, usually called `cls`, instead of an instance. It's defined with `@classmethod` and can read or change **class attributes**.

```py
class Person:
    total_people = 0  # Class attribute

    def __init__(self, name):
        self.name = name
        Person.total_people += 1

    @classmethod
    def get_total_people(cls):
        return cls.total_people


Person("Alice")
Person("Bob")
print(Person.get_total_people())  # 2
```

## 📝 Instructions:

1. Create a class called `CircleCalculator` with a class attribute `pi` equal to `3.14159`.

2. Add a class method `calculate_area(radius)` that **returns** `pi * radius ** 2`, reading `pi` through `cls`.

3. Call the method on the class, without creating an instance, and print the result.

## 📎 Example:

```py
print(CircleCalculator.calculate_area(5))  # 78.53975
```

## 💡 Hints:

+ Write `@classmethod` above the method, and use `cls` as its first parameter.

+ Compare it with the previous exercise: a static method doesn't receive `cls`, so it can't use class attributes in a flexible way.
