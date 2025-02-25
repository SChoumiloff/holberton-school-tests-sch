from typing import List

class Bank:
    """
        Bank class for leetcode problem 2043
    """
    def __init__(self, balance: list[int]):
        self.balance = balance

    def is_valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_account(account1) or not self.is_valid_account(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True



if __name__ == "__main__":
    account_values: List[int] = [10, 100, 20, 50, 30]
    operations: List[str] = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    params: List[List[int]] = [[[10,100,20,50,30]],[3,10],[5,1,20],[5,20],[3,4,15],[10,50]]

    
    results = []
    bank = None
    
    for i, operation in enumerate(operations):
        if operation == "Bank":
            bank = Bank(params[i][0])
            results.append(None)
        elif operation == "withdraw":
            results.append(bank.withdraw(params[i][0], params[i][1]))
        elif operation == "transfer":
            results.append(bank.transfer(params[i][0], params[i][1], params[i][2]))
        elif operation == "deposit":
            results.append(bank.deposit(params[i][0], params[i][1]))
    
    print(results)