# `013` Abstract Classes

An **abstract class** is a class that can't be instantiated: it only defines which methods its child classes **must** implement. In Python you create it with the `abc` module:

```py
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof"


print(Dog().sound())  # Woof
Animal()  # TypeError: Can't instantiate abstract class Animal
```

## 📝 Instructions:

1. Create an abstract class `PaymentMethod` with an abstract method `pay(amount)`.

2. Create a class `CreditCard(PaymentMethod)` that stores `card_number`. Its `pay(amount)` **returns** `"Paid <amount> with card ending in <last 4 digits>"`.

3. Create a class `PayPal(PaymentMethod)` that stores `email`. Its `pay(amount)` **returns** `"Paid <amount> with PayPal account <email>"`.

## 📎 Example:

```py
card = CreditCard("4111222233334444")
print(card.pay(50))  # Paid 50 with card ending in 4444

paypal = PayPal("ana@example.com")
print(paypal.pay(20))  # Paid 20 with PayPal account ana@example.com

PaymentMethod()  # TypeError
```

## 💡 Hint:

+ `card_number[-4:]` gives you the last 4 characters of a string.
