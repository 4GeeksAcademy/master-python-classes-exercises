# `014` Dataclasses

Muchas clases solo guardan datos. El decorador `@dataclass` escribe `__init__`, `__repr__` y `__eq__` por ti, a partir de los atributos que declares con anotaciones de tipo:

```py
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int = 0  # Default value


print(Point(1, 2))  # Point(x=1, y=2)
print(Point(1) == Point(1, 0))  # True
```

## 📝 Instrucciones:

1. Crea una dataclass `Product` con los campos `name: str`, `price: float` y `quantity: int` (por defecto `0`).

2. Añade un método `total_value()` que **retorne** `price * quantity`.

## 📎 Ejemplo:

```py
laptop = Product("Laptop", 999.99, 2)
print(laptop)  # Product(name='Laptop', price=999.99, quantity=2)
print(laptop.total_value())  # 1999.98
print(Product("Mouse", 20.0))  # Product(name='Mouse', price=20.0, quantity=0)
```

## 💡 Pista:

+ Los campos con valor por defecto deben ir después de los campos que no lo tienen.
