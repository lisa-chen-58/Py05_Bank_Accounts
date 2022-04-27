class BankAccount:
    all_accounts=[]
    def __init__(self, int_rate=0.03, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance < 0:
            print('Insufficient funds')
        else:
            self.balance *= self.int_rate

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self,name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02,1000),
            "savings" : BankAccount(.05,3000)
        }

    def display_user_balance(self):
        # print(f"{self.name}'s checking balance is {self.account['checking'].display_account_info()} and savings balance is {self.account['savings']}")
        # return self
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")

lisa = User("Lisa")
saria = User("Saria")
lisa.account['checking'].deposit(100)
saria.account['savings'].deposit(2000)
lisa.display_user_balance()
saria.display_user_balance()


