class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def getBalance(self):
        return self.__balance


account = BankAccount("50213721101", 100000)
sbiAccount = BankAccount("78645213465", 5000000)
account.deposit(5000)
account.withdraw(2000)
sbiAccount.deposit(100000)
sbiAccount.withdraw(300000)

print("Current balance:", account.getBalance())
print("Current balance in SBI account :", sbiAccount.getBalance())