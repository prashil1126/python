class Account:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return "Amount Deposited"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Funds unavailable"
        else:
            self.balance -= amount
            return "Amount Withdrawn"

    def __str__(self):
        return "Account owner : {} \nAccount balance:${}".format(self.owner_name, self.balance)


acc1 = Account("Jose", 100)
print(acc1)
print(acc1.deposit(50))
print(acc1.balance)
print(acc1.withdraw(75))
print(acc1.balance)
print(acc1.withdraw(175))

