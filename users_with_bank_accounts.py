class BankAccount:
    all_checking=[]
    def __init__(self, int_rate=0.03, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_checking.append(self)

    @classmethod
    def checkings_all(cls):
        sum = 0
        for checking in cls.all_checking:
            print(checking.balance, checking.int_rate)
            sum+=1


class User:

    def __init__(self, first_name, last_name, checking_bal = 0, savings_bal = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.checking = BankAccount(0.03,checking_bal)
        self.savings = BankAccount(0.04, savings_bal)

    # Applying interest
    def apply_interest(self,account):
        if account == "checking":
            if self.checking.balance > 0:
                self.checking.balance += (self.checking.balance * self.checking.int_rate)
            return self

        elif account == "savings":
            if self.savings.balance > 0:
                self.savings.balance += (self.savings.balance * self.savings.int_rate)
            return self


    # User deposits money into checking
    def deposit_checking(self, amount):
        self.checking += amount
        print(f"${amount} has been deposited")
        return self
        
    # User deposits money into savings
    def deposit_savings(self, amount):
        self.savings += amount
        print(f"${amount} has been deposited")
        return self
        
    # User withdraws money from checking
    def withdraw_checking(self, amount):
        if self.checking.balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.checking.balance -= 5
            
        else:
            self.checking.balance -= amount
        return self

    # User withdraws money from savings
    def withdraw_savings(self, amount):
        if self.savings < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.savings -= 5
            
        else:
            self.savings -= amount
        return self

    # Transfer checking to savings
    def transfer(self,user,amount):
        self.checking.balance -= amount
        user.checking.balance += amount
        print(f"{self.first_name} transferred ${amount} to {user.first_name}")
        return self

    # User Transfer
    def user_transfer(self, user, amount):
        self.checking.balance -= amount
        user.checking.balance += amount
        print(f"{self.first_name} has transferred ${amount} to {user.first_name}")
        return self

    # Display Balances
    def display_user_balance(self):
        print(f"You have ${self.checking.balance} in your Checkings Account and ${self.savings.balance} in your savings account")
        return self

lisa = User("Lisa","Chen", 1000,5000)
saria = User("Saria","Dog","500","1000")
lisa.display_user_balance().apply_interest("savings").display_user_balance()