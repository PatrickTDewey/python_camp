class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) > 0:
            self.balance -= amount
        else:
            print('Insufficient Funds')
        return self


class CheckingAccount(BankAccount):
    pass


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount, is_early):
        if is_early:
            amount *= 1.10
        super().withdraw(amount)
        return self
