# `004` Class Attributes

Attributes created with `self.` inside `__init__` belong to **each instance**. Attributes defined directly in the class body belong to the **class** and are shared by every instance:

```py
class Bicycle:
    wheels = 2  # Class attribute: shared by all bicycles

    def __init__(self, color):
        self.color = color  # Instance attribute: different for each bicycle


print(Bicycle.wheels)  # 2
print(Bicycle("red").wheels)  # 2
```

## 📝 Instructions:

1. Create a class called `Car` with a **class attribute** `wheels` equal to `4`.

2. Its `__init__` receives and stores the instance attributes `brand` and `model`.

3. Add a method `description()` that **returns** `"<brand> <model> with <wheels> wheels"`, reading `wheels` from the class attribute.

## 📎 Example:

```py
car = Car("Toyota", "Corolla")
print(car.description())  # Toyota Corolla with 4 wheels
print(Car.wheels)  # 4
```

## 💡 Hint:

+ Inside a method you can read a class attribute with `self.wheels` or `Car.wheels`.
