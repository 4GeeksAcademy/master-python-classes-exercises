class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The deposit must be greater than 0")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("The withdrawal must be greater than 0")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


account = BankAccount("Ana", 100)
account.deposit(50)
account.withdraw(30)
print(account.balance)
