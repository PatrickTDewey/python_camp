# class User:
#     bank_name = 'First National National Nationale'
#     def __init__(self):
#         self.name = 'Patrick'
#         self.email = 'ptddev@protonmail.com'
#         self.account_balance = 1000

# michael = User()
# anna = User()
# print(michael.name, anna.name)

# michael.name = 'Michael'
# anna.name = 'anna'
# print(michael.name, anna.name)

# print(michael.bank_name)

# User.bank_name = 'Second Nationale Natties'
# print(michael.bank_name)

# michael.bank_name = 'Jerrys Bank & Loan'
# anna.bank_name = 'gorgeous bank'
# User.bank_name = 'Bear Grills Bank'
# print(michael.bank_name, anna.bank_name, User.bank_name)
class User:
    bank_name = 'Bank of Patricio'
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        # account balance is set to 0
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'User: {self.name} \nBalance: ${self.account_balance}')
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
        return self
patrick = User('Patrick', 'ptddev@protonmail.com')
# print(patrick.email_address)
# print(patrick.account_balance)
# patrick.make_deposit(100)
# print(patrick.account_balance)
# patrick.make_withdrawl(50)
# print(patrick.account_balance)
# patrick.display_user_balance()
nick = User('Nick', 'nick@nickmail.com')
spencer = User('Spencer', 'spencer@spencer.com')
patrick.make_deposit(100).make_deposit(100).make_deposit(100).display_user_balance().transfer_money(nick, 100).display_user_balance()
nick.display_user_balance().transfer_money(spencer, 50).display_user_balance()
spencer.display_user_balance()



