# `011` Properties and Encapsulation

**Encapsulation** means protecting the internal data of an object so it can only change in valid ways. In Python:

+ An attribute starting with `_` (like `_balance`) means "internal: don't touch it from outside".
+ The `@property` decorator lets you read a method as if it were an attribute, without allowing direct assignment.

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

To report an invalid operation, a method can **raise** an exception: `raise ValueError("message")`.

## 📝 Instructions:

1. Create a class `BankAccount` whose `__init__` receives `owner` and an optional `balance` (default `0`). Store the balance in `_balance`.

2. Add a read-only property `balance` that **returns** `_balance`.

3. Add a method `deposit(amount)` that adds the amount to the balance. If `amount` is `0` or negative, raise `ValueError`.

4. Add a method `withdraw(amount)` that subtracts the amount. If `amount` is `0` or negative, or greater than the balance, raise `ValueError`.

## 📎 Example:

```py
account = BankAccount("Ana", 100)
account.deposit(50)
account.withdraw(30)
print(account.balance)  # 120

account.withdraw(500)  # ValueError
account.balance = 1000000  # AttributeError
```

## 💡 Hint:

+ Default values go in the parameter list: `def __init__(self, owner, balance=0):`.
