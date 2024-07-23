class Bank:
    accHolderName = "" # instance variable
    balance = 0
    __COUNT = 0

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def __init__(self,myname=None,mybal=None):
        if(myname is not None):
            self.accHolderName=myname
        if(mybal is not None):
            self.balance=mybal
        Bank.__COUNT +=1 #static variable

    @staticmethod
    def TotalAccounts():
        print("Total Accounts in the back are {}".format(Bank.__COUNT))

    # distrcutor method
    def __del__(self):
        print("{} is deleted".format(self.accHolderName))
        Bank.__COUNT -=1


class Savings(Bank):
    isSalariedEmployee=True

    # inheritance
    def __init__(self,name,bal,isWorking):
        super().__init__(name,bal)
        self.isSalariedEmployee=isWorking

b = Bank()
b.accHolderName = 'Pavan'
print(b.accHolderName)

b1 = Bank()
setattr(b1, "accHolderName","Python with Pavan")
print(getattr(b1, "accHolderName"))

b2 = Bank("John",20000)
b2.withdraw(5000)

b2.deposit(3000)
print("Account holder name is {} and Balance is {}".format(b2.accHolderName,b2.balance))

print(b.__doc__)
# print(Bank.__COUNT)
Bank.TotalAccounts()

# del b
# del b1
Bank.TotalAccounts()

s = Savings("Martin",30000,True)
print("Account holder name is {} and Balance is {} and working {}".format(s.accHolderName,s.balance,s.isSalariedEmployee))

Bank.TotalAccounts()