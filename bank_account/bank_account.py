from __future__ import annotations


class BankAccount:

    def __init__(self, balance: int = 0) -> None:
        self.balance = balance
        
    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount
    
    def transfer(self, other_account: BankAccount, amount: int) -> None:
        other_account.deposit(amount)
        self.withdraw(amount)

    def __repr__(self) -> str:
        return f"BankAccount(balance={self.balance})"
