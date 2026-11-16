# `014` Dataclasses

Many classes only store data. The `@dataclass` decorator writes `__init__`, `__repr__` and `__eq__` for you, based on the attributes you declare with type hints:

```py
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int = 0  # Default value


print(Point(1, 2))  # Point(x=1, y=2)
print(Point(1) == Point(1, 0))  # True
```

## 📝 Instructions:

1. Create a dataclass `Product` with the fields `name: str`, `price: float` and `quantity: int` (default `0`).

2. Add a method `total_value()` that **returns** `price * quantity`.

## 📎 Example:

```py
laptop = Product("Laptop", 999.99, 2)
print(laptop)  # Product(name='Laptop', price=999.99, quantity=2)
print(laptop.total_value())  # 1999.98
print(Product("Mouse", 20.0))  # Product(name='Mouse', price=20.0, quantity=0)
```

## 💡 Hint:

+ Fields with a default value must go after the fields without one.
