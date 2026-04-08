from abc import ABC, abstractmethod

# abstraction
class BankSystem(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# class + encapsulation + inheritance combines
class BankAccount(BankSystem):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance 
    # Deposit method
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully.")

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # getter method
    def get_balance(self):
        return self.__balance

    # display
    def display(self):
        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Balance:", self.__balance)


#object creation 
account1 = BankAccount("Rahul", 1000)

account1.display()

account1.deposit(500)
account1.withdraw(300)

print("Current Balance:", account1.get_balance())