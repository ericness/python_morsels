from __future__ import annotations
from typing import List


class BankAccount:
    accounts: List[BankAccount] = []

    def __init__(self, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self._balance = balance
        if BankAccount.accounts:
            self.number = max(account.number for account in BankAccount.accounts) + 1
        else:
            self.number = 1000
        BankAccount.accounts.append(self)
    
    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        if amount > self._balance:
            raise ValueError(f"Can't withdraw {amount} with {self._balance} balance")
        self._balance -= amount

    def transfer(self, other_account: BankAccount, amount: int) -> None:
        self.withdraw(amount)
        other_account.deposit(amount)

    def __repr__(self) -> str:
        return f"BankAccount(balance={self._balance},number={self.number})"
