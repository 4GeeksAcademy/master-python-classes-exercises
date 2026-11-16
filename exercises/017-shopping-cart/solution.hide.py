from dataclasses import dataclass


@dataclass
class CartItem:
    name: str
    price: float
    quantity: int = 1

    def subtotal(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = CartItem(name, price, quantity)

    def remove_item(self, name):
        del self.items[name]

    def total(self):
        return round(sum(item.subtotal() for item in self.items.values()), 2)

    def __len__(self):
        return sum(item.quantity for item in self.items.values())


cart = ShoppingCart()
cart.add_item("apple", 0.5, 4)
cart.add_item("bread", 2.25)
cart.add_item("apple", 0.5, 2)
print(cart.items["apple"])
print(len(cart))
print(cart.total())
