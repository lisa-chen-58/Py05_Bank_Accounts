from bankaccountNew import BankAccount

class User:

    def __init__(self, name="Unassigned"):
        self.name = name
        self.bank_accounts = {}

    def create_account(self, bank_type, int_rate, balance):
        name = BankAccount(bank_type, int_rate, balance);
        self.bank_accounts[bank_type] = name
        print(f"{self.name}'s {self.bank_accounts[bank_type].bank_type} account created")
        return self;

    def make_deposit(self, bank_type, amount):
        self.bank_accounts[bank_type].balance += amount;
        print(f"{self.name}'s deposit to {self.bank_accounts[bank_type].bank_type} was successful!")
        return self;
    
    def make_withdrawal(self, key, amount):
        if(self.bank_accounts[key].balance < amount):
            print(f"{self.name}, there are not enough funds. You're current funds are at {self.bank_accounts[key].balance}")
        else:
            self.bank_accounts[key].balance -= amount;
            print(f"{self.name}'s withdrawal from {self.bank_accounts[key].bank_type} was successful!")
        return self;

    def display_user_balance(self, key):
        print(f"{self.name}'s {self.bank_accounts[key].bank_type} has an interest of {self.bank_accounts[key].int_rate} and a balance of {self.bank_accounts[key].balance}")
        return self;
    
    def transfer_money(self, key, amount, other_user, other_key):
        if(self.bank_accounts[key].balance < amount):
            print(f"{self.name}'s account is insufficient")
        else:
            self.bank_accounts[key].balance -= amount;
            other_user.bank_accounts[other_key].balance += amount;
        return self

    @classmethod
    def display_all(cls):
        for account in cls.bank_accounts:
            print(account.items())


lisa = User("Lisa")
lisa.create_account("debit",0.02,1000).make_deposit("debit",1000).make_withdrawal("debit",50).display_user_balance("debit")

bryan = User("Bryan")
bryan.create_account("credit",0.01,2000)

lisa.transfer_money("debit",100,bryan,"credit")

lisa.display_user_balance("debit")
bryan.display_user_balance("credit")

