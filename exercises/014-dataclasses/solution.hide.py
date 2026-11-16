from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_value(self):
        return self.price * self.quantity


laptop = Product("Laptop", 999.99, 2)
print(laptop)
print(laptop.total_value())
