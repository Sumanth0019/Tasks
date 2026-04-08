#bank balance using the encapsulation 

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


# Object
account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

print("Balance:", account.get_balance())