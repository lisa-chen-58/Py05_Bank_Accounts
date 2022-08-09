class BankAccount:
    # don't forget to add some default values for these parameters!
    type = "debit"
    bank_accounts = [] 

    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate;
        self.balance = balance;
        BankAccount.bank_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount;
        return self;

    def withdraw(self, amount):
        if(self.balance < amount):
            print(f"Account balance at {self.balance} is not high enough for a {amount} withdrawal")
            print("Charging a $5 fee")
            self.balance -= 5;
            return self;
        else:
            self.balance -= amount;
            return self;

    def display_account_info(self):
        print(f"Type: Interest Rate: {self.int_rate} \n Balance: {self.balance}")
        return self;

    def yield_interest(self):

        if(self.balance >0):
            self.balance = self.balance + (self.balance * self.int_rate);
            return self;
        else:
            print("No balance to yield interest")
            return self;

    @classmethod
    def all_balances(cls):
        for account in cls.bank_accounts:
            account.display_account_info()
            
# Create a BankAccount class with the attributes interest rate and balance. done.
# Add a deposit method to the BankAccount class done.
# Add a withdraw method to the BankAccount class done.
# Add a display_account_info method to the BankAccount class done.
# Add a yield_interest method to the BankAccount class

# Create 2 accounts
becu = BankAccount(0.01,2000);

citi = BankAccount(0.03, 3000);

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
print("BECU")
becu.deposit(300).deposit(200).deposit(100).withdraw(50).display_account_info().yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
print("\n CITI")
citi.deposit(400).deposit(1000).withdraw(50).withdraw(100).withdraw(2000).withdraw(3000).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
print("\n All Accounts")
BankAccount.all_balances()