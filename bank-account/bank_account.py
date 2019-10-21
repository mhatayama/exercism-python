from threading import Lock


class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.isOpen = False
        self._lock = Lock()

    def get_balance(self):
        if not self.isOpen:
            raise ValueError("Invalid")
        return self.balance

    def open(self):
        if self.isOpen:
            raise ValueError("Invalid")
        self.isOpen = True

    def deposit(self, amount):
        if not self.isOpen or amount < 0:
            raise ValueError("Invalid")
        with self._lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.isOpen or amount < 0 or self.balance - amount < 0:
            raise ValueError("Invalid")
        with self._lock:
            self.balance -= amount

    def close(self):
        if not self.isOpen:
            raise ValueError("Invalid")
        self.isOpen = False
        self.balance = 0
