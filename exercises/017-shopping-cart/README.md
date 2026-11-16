# `017` Final Challenge: Shopping Cart

Time to combine what you learned: a dataclass, composition, special methods and exceptions, all in a small shopping cart.

## 📝 Instructions:

1. Create a dataclass `CartItem` with the fields `name: str`, `price: float` and `quantity: int` (default `1`), and a method `subtotal()` that **returns** `price * quantity`.

2. Create a class `ShoppingCart` whose `__init__` creates an empty dictionary `items` (keys are product names, values are `CartItem` objects).

3. `add_item(name, price, quantity=1)`: if the product is already in the cart, increase its quantity; otherwise, add a new `CartItem`.

4. `remove_item(name)`: remove the product. If it isn't in the cart, raise `KeyError`.

5. `total()`: **return** the sum of all subtotals, rounded to 2 decimals.

6. `__len__`: **return** the total number of units in the cart (the sum of all quantities).

## 📎 Example:

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

## 💡 Hints:

+ Reuse `subtotal()` inside `total()`: `sum(item.subtotal() for item in self.items.values())`.

+ `del self.items[name]` already raises `KeyError` if the key doesn't exist.
