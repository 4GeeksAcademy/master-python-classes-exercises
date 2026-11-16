# `008` Static Methods

A **static method** belongs to a class but doesn't receive `self` or the class: it's a regular function grouped inside the class because it's related to it. You define it with the `@staticmethod` decorator and usually call it on the class itself.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18


print(Person.is_adult(25))  # True
print(Person.is_adult(16))  # False
```

## 📝 Instructions:

1. Create a class called `MathOperations`.

2. Add a static method `add_numbers(a, b)` that **returns** the sum of both numbers.

3. Add a static method `is_even(number)` that **returns** `True` if the number is even and `False` otherwise.

4. Call both methods directly on the class (without creating an instance) and print the results.

## 📎 Example:

```py
print(MathOperations.add_numbers(10, 15))  # 25
print(MathOperations.is_even(7))  # False
```

## 💡 Hint:

+ Write `@staticmethod` on the line right above each method definition.
