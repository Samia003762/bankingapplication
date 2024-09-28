class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        print(f"Account balance for {self.holder_name}: {self.balance}")
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print(f"Overdraft limit reached. Available balance: {self.balance + self.overdraft_limit}")

def transfer_funds(from_account, to_account, amount):
    if amount > 0 and from_account.get_balance() >= amount:
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Transferred {amount} from {from_account.holder_name} to {to_account.holder_name}")
    else:
        print("Transfer failed due to insufficient funds or invalid amount.")

if __name__ == "__main__":
    print("Implementation of code: ")
    savanah_savings = SavingsAccount("001", "Savanah Micheals", 1000)
    kai_checking = CheckingAccount("002", "Kai Cooper", 500)
    
    savanah_savings.get_balance()
    kai_checking.get_balance()
    
    savanah_savings.deposit(200)
    kai_checking.withdraw(100)
    
    transfer_funds(savanah_savings, kai_checking, 300)
    
    savanah_savings.add_interest()

    savanah_savings.get_balance()
    kai_checking.get_balance()
