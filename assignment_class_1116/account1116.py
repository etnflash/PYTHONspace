class Account:

  def __init__(self, account = None, balance = 0, interestRate = 0):
    self.__account = account
    self.__balance = balance
    self.__interestRate = interestRate

  def setAccount(self, account):
    self.__account = account

  def getAccount(self):
    return self.__account

  def getBalance(self):
    return self.__balance

  def calculateInterest(self):
    return self.__interestRate * self.__balance / 100

  def deposit(self, money):
    self.__balance += money

  def withdraw(self, money):
    self.__balance -= money

  def setBalance(self, balance):
    self.__balance = balance

  def setInterestRate(self, interestRate):
    self.__interestRate = interestRate



acc = Account("441-0290-1203", 500000, 7.3)
# print(acc.getAccount())
print(f"계좌정보: {acc.getAccount()} 현재잔액: {acc.getBalance()}")
acc.deposit(20000)
print(f"계좌정보: {acc.getAccount()} 현재잔액: {acc.getBalance()}")

print(f"이자: {acc.calculateInterest()}")