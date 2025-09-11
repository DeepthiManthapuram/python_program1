class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
    
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance = self.__balance - amount
        return self.__balance

    def get_balance(self):
        return self.__balance

obj = BankAccount()
obj.deposit(5000)
obj.withdraw(2000)
print("Balance:",obj.get_balance())