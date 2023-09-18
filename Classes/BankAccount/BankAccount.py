


class BankAccount:
    def __init__(self,account_number=0, account_holder=0, account_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0 and isinstance(amount, (int, float)):
            self.account_balance += amount
            return self.account_balance
        else:
            print("An error has occurred")
            return 0
    
    def withdraw(self, amount):
        if amount > 0 and isinstance(amount, (int, float)):
            if amount <= self.account_balance:
                self.account_balance -= amount
                return self.account_balance
            else:
                return 0
        else:
            print("An error has occurred")
            return 0
    
    def transfer(self, amount):
        
        return 0
    
    def get_account_balance(self):
        return f"{self.account_balance}"
    
    def get_account_details(self):
        return f"{self.account_number} {self.account_holder} {self.account_balance}"