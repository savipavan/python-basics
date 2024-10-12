###################userh.py
# Bank User has name and account. There are two types of Users
# Normal and privileged user . There are two types of privileged
# users, Gold and Silver. Gold has cashback of 5% and Silver has
# cashback of 3% of expenditure when they spend any cash

"""
Nouns
    classes
Verbs
    methods of those classes

Relations
    has/have - containment - taking those/creating in __init__
    is/are  - inheritance - class Child(Baseclass)

Special methods
    internal method
    used by python to do certain operator/activity
    signature fixed, given in datamodel

self
    not a keyword
    python puts instance in the first arg
    by convention

dynamic vs static
    typed based checking happens at runtime vs compile time
    in Py - no overloading possible

OOP
    no access control
    instance variable and method
        method - first arg is instance
    class variable and method ( equiv to java static)
        method - first arg is class
        can not access any instance variable
        can only access class variable
    static method
        there is no first arg
        generally used for NS
    property
    no abstract key word or no interface
    but has Abstract class , implemented  metaclass
    Has metaclass
        metaclass is a class which creates other classes
        type is default metaclass
        Metaprogramming
            inherits from type and does
            class creation level manipulation
    slots etc
    - Refer Learning Python - Mark Lutz

"""
DEBUG = False
def d_print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

# inherit from Exception
class NotEnoughBalance(Exception):
    pass

class BankAccount:
    def __init__(self, initAmount):   #special method 1
        d_print("BankAccount.__init__")
        self.amount = initAmount    #instance variable, any method can update and access in this class
        #a = 0                       #simple var, scope is only this method
    def __str__(self):              #special method 2
        d_print("BankAccount.__str__")
        return f"BankAccount({self.amount})"
    def transact(self, amount):         #3 # public method
        d_print("BankAccount.transact")
        if self.amount + amount < 0:
            raise NotEnoughBalance("not possible")
        self.amount += amount

    #has relation
#GOLD - 5% cashback , Silver-2% , Normal = 0%
#GoldUser,Silver, Normal OR  BankUser - where to put?
#Design Pattern - Template - algorith in base class, tweaking in derived
class BankUser:
    def __init__(self, name, initAmount):
        d_print("BankUser.__init__")
        self.name = name
        self.account = BankAccount(initAmount)
    def __str__(self):
        d_print("BankUser.__str__")
        return f"BankUser({self.name}, {self.account})"
    def transact(self, amount):
        d_print("BankUser.transact")
        try:
            self.account.transact(amount)
            if amount < 0:
                cashback = self.get_cashback_percentage() * abs(amount)
                self.account.transact(cashback)
        except NotEnoughBalance as ex:
            print(self.name, str(ex), amount)
    def get_cashback_percentage(self):
        return 0

    #there are three bankusers
class NormalUser(BankUser):
    pass

class GoldUser(BankUser):
    def get_cashback_percentage(self):
        return 0.05

class SilverUser(BankUser):
    def get_cashback_percentage(self):
        return 0.03


    #f"" - # format string
if __name__ == '__main__':   # pragma: no cover
    users = [GoldUser("Gold", 100),
             SilverUser("Silver", 100),
             NormalUser("Normal", 100)]
    amounts = [100, -200, 300, -400, 400]
    for user in users:
        for am in amounts :
            d_print(user, "for", am)
            user.transact(am)
        print(user)




    #ba = BankUser("abc", 100)   #BankUser.__init__( ba,"abc", 100)
    #ba.transact(100)
    #print(ba)               #BankUser.__str__(ba)       #BankAccount(200)