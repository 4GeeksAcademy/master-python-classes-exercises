from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid {amount} with card ending in {self.card_number[-4:]}"


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid {amount} with PayPal account {self.email}"


print(CreditCard("4111222233334444").pay(50))
print(PayPal("ana@example.com").pay(20))
