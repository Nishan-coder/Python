class MinimumBalanceError(Exception):
  pass
class Account:
  accnumber=5051
  def __init__(self,name,balance=1000):
    if balance<1000:
      raise MinimumBalanceError('Account Cannot be created')
    self.name=name
    self.balance=balance
    self.account_number=Account.accnumber
    Account.accnumber+=1

  def deposit(self,amount):
   self.balance += amount
   return self.balance

  def withdraw(self,amount):
    if self.balance-amount<1000:
      raise MinimumBalanceError('Minimum balance should be 1000')
    self.balance -= amount
    return self.balance

  def showdata(self):
    print(self.name)
    print(self.account_number)
    print(self.balance)

try:
  a1=Account('Nishan',10000)
  a1.showdata()
  print('')
  a1.withdraw(9100)
  a1.showdata()

except MinimumBalanceError as e:
  print(e)
  print('')
