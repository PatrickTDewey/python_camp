class BankAccount:
    # class attribute
    bank_name = 'First National Taco Bank'
    all_accounts = []

    def __init__(self, account_name, int_rate, balance=0):
        self.account_name = account_name
        self.int_rate = float(int_rate)
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        # we can use the static method here to evaluate
        # if we can withdrawl the funds without going negative
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= -5
        return self

    def display_account_info(self):
        print(
            f"Bank {self.bank_name}\nBalance: {self.balance}\nInterest Rate: {self.int_rate}\n")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print('cannot gain interest when you are broke...')
        return self
    # static methods have no access to any atribute
    # only to what is passed into it

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) > 0:
            return True
        else:
            return False
    # class method to change the name of the bank

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    # class method to get balance of all accounts

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance

        return sum

    @classmethod
    def all_account_info(cls):
        # for i in range(len(cls.all_accounts)):
        #     cls.all_accounts[i].display_account_info()
        for i, v in enumerate(cls.all_accounts, 0):
            print((i, v.display_account_info()))


class User:
    def __init__(self, name, email_address):
        self.account_list = []
        self.name = name
        self.email_address = email_address
        # account balance is set to 0

    def create_account(self, name, int_rate, balance):
        self.account = BankAccount(name, int_rate, balance)
        self.account_info = {
            'bank_name': self.account.bank_name,
            'account_name': self.account.account_name,
            'interest_rate': self.account.int_rate,
            'balance': self.account.balance
        }
        self.account_list.append(self.account_info)
        return self

    def make_deposit(self, name, amount):
        for i in range(len(self.account_list)):
            if self.account_list[i]['account_name'] == name:
                self.account.deposit(amount)
                print(self.account.display_account_info())
                self.account_list[i]['balance'] = self.account.balance
                return self
            else:
                print('No account with that name found')
                return self

    def make_withdrawl(self, name, amount):
        for i in range(len(self.account_list)):
            if self.account_list[i]['account_name'] == name:
                self.account.withdraw(amount)
                print(self.account.display_account_info())
                self.account_list[i]['balance'] = self.account.balance
                break
            else:
                print('No account with that name found')
            return self

    def display_user_balance(self):
        print(f'User: {self.name} \nBalance: ${self.account.balance}')
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


patrick = User('Patrick', 'ptddev@protonmail.com')
patrick.create_account('Checking', 0.01, 100)
patrick.create_account('Savings', 0.05, 300)
patrick.make_deposit('Checking', 100).make_withdrawl('Checking', 100)
print(patrick.account_list)
# print(patrick.display_user_balance())
# print(patrick.account_list)
