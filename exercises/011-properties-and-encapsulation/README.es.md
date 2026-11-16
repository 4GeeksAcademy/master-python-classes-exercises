# `011` Propiedades y encapsulamiento

El **encapsulamiento** consiste en proteger los datos internos de un objeto para que solo cambien de formas válidas. En Python:

+ Un atributo que empieza con `_` (como `_balance`) significa "interno: no lo toques desde fuera".
+ El decorador `@property` te permite leer un método como si fuera un atributo, sin permitir la asignación directa.

```py
class Thermometer:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius


t = Thermometer()
print(t.celsius)  # 0 (no parentheses)
t.celsius = 50  # AttributeError: it's read-only
```

Para avisar de una operación inválida, un método puede **lanzar** una excepción: `raise ValueError("message")`.

## 📝 Instrucciones:

1. Crea una clase `BankAccount` cuyo `__init__` reciba `owner` y un `balance` opcional (por defecto `0`). Guarda el saldo en `_balance`.

2. Añade una propiedad de solo lectura `balance` que **retorne** `_balance`.

3. Añade un método `deposit(amount)` que sume la cantidad al saldo. Si `amount` es `0` o negativo, lanza `ValueError`.

4. Añade un método `withdraw(amount)` que reste la cantidad. Si `amount` es `0` o negativo, o mayor que el saldo, lanza `ValueError`.

## 📎 Ejemplo:

```py
account = BankAccount("Ana", 100)
account.deposit(50)
account.withdraw(30)
print(account.balance)  # 120

account.withdraw(500)  # ValueError
account.balance = 1000000  # AttributeError
```

## 💡 Pista:

+ Los valores por defecto van en la lista de parámetros: `def __init__(self, owner, balance=0):`.
