# `005` The `__repr__` and `__eq__` Methods

By default, two different objects are never equal, even with the same data, and printing them shows something like `<__main__.Point object at 0x7f...>`. Two special methods fix that:

+ `__repr__` returns a text for developers, usually showing how to recreate the object. It's used in the console and inside lists.
+ `__eq__(self, other)` defines when two objects are equal with `==`.

## 📝 Instructions:

1. Create a class called `Point` whose `__init__` stores `x` and `y`.

2. Add a `__repr__` method that **returns** `"Point(<x>, <y>)"`.

3. Add an `__eq__` method that **returns** `True` when the other object is also a `Point` with the same `x` and `y`, and `False` otherwise.

## 📎 Example:

```py
a = Point(1, 2)
b = Point(1, 2)
print(a)  # Point(1, 2)
print([a, Point(0, 0)])  # [Point(1, 2), Point(0, 0)]
print(a == b)  # True
print(a == Point(2, 1))  # False
print(a == "Point(1, 2)")  # False
```

## 💡 Hint:

+ `isinstance(other, Point)` checks if `other` is a `Point`.
