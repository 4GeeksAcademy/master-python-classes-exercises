# `017` Reto final: carrito de compras

Es hora de combinar lo que aprendiste: una dataclass, composición, métodos especiales y excepciones, todo en un pequeño carrito de compras.

## 📝 Instrucciones:

1. Crea una dataclass `CartItem` con los campos `name: str`, `price: float` y `quantity: int` (por defecto `1`), y un método `subtotal()` que **retorne** `price * quantity`.

2. Crea una clase `ShoppingCart` cuyo `__init__` cree un diccionario vacío `items` (las claves son nombres de productos y los valores son objetos `CartItem`).

3. `add_item(name, price, quantity=1)`: si el producto ya está en el carrito, aumenta su cantidad; si no, añade un nuevo `CartItem`.

4. `remove_item(name)`: elimina el producto. Si no está en el carrito, lanza `KeyError`.

5. `total()`: **retorna** la suma de todos los subtotales, redondeada a 2 decimales.

6. `__len__`: **retorna** el número total de unidades en el carrito (la suma de todas las cantidades).

## 📎 Ejemplo:

```py
cart = ShoppingCart()
cart.add_item("apple", 0.5, 4)
cart.add_item("bread", 2.25)
cart.add_item("apple", 0.5, 2)

print(cart.items["apple"])  # CartItem(name='apple', price=0.5, quantity=6)
print(len(cart))  # 7
print(cart.total())  # 5.25

cart.remove_item("bread")
print(cart.total())  # 3.0
```

## 💡 Pistas:

+ Reutiliza `subtotal()` dentro de `total()`: `sum(item.subtotal() for item in self.items.values())`.

+ `del self.items[name]` ya lanza `KeyError` si la clave no existe.
