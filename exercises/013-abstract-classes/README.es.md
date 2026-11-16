# `013` Clases abstractas

Una **clase abstracta** es una clase que no se puede instanciar: solo define qué métodos **deben** implementar sus clases hijas. En Python se crea con el módulo `abc`:

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

## 📝 Instrucciones:

1. Crea una clase abstracta `PaymentMethod` con un método abstracto `pay(amount)`.

2. Crea una clase `CreditCard(PaymentMethod)` que guarde `card_number`. Su `pay(amount)` **retorna** `"Paid <amount> with card ending in <last 4 digits>"`.

3. Crea una clase `PayPal(PaymentMethod)` que guarde `email`. Su `pay(amount)` **retorna** `"Paid <amount> with PayPal account <email>"`.

## 📎 Ejemplo:

```py
card = CreditCard("4111222233334444")
print(card.pay(50))  # Paid 50 with card ending in 4444

paypal = PayPal("ana@example.com")
print(paypal.pay(20))  # Paid 20 with PayPal account ana@example.com

PaymentMethod()  # TypeError
```

## 💡 Pista:

+ `card_number[-4:]` te da los últimos 4 caracteres de un string.
