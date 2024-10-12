###################userh.py
# Bank User has name and account. There are two types of Users
# Normal and privileged user . There are two types of privileged
# users, Gold and Silver. Gold has cashback of 5% and Silver has
# cashback of 3% of expenditure when they spend any cash

"""
nouns can be class
verbs"
    methods of those class

relations:
    has/have - containment - taking those/creating in __init__
    is/are  - inheritance - class Child(Baseclass)

Question 1) -how many methods? either 3 or 1 when we see def is actually a method
special methods : are internal methods used by python to do certain activities
signature fixed, names fixed, which we cannot change: https://docs.python.org/3/reference/datamodel.html

def __init__(self, initAmount):  # 1 methods, 2 arguments
        self.amount = initAmount

    What could be the self and initAmount. 100 is initAmount
    What would be the self, self is the object
    ba = BankAccount(100) # BankAccount.__init__(ba,100) # It is called creating instance

    def transact(self, amount):  #BankAccount.__transact(ba,100)


Question : is self is a keyword?
Ans: not a keyword
    python puts instance in the first argument, self should be the first argument
    by convention
    class, def are keyword

in java this (keyword) , java self is not a keyword(explict).

How inheritance works?
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

d = D()
D.__init__(d)
d.any_var

In inheritance is something called Method resolution order - MRO
Using internal attributes
check what is the class of d
d.__class__

# to check the method resolution order we need to see in class
d.__class__.__mro__

# Object is root of all class. dir(object) brings the method

# out of the class can have the variable A.any_var = 20 and d.any_var will get the attribute, it will found in A
# D.any_var = 200 will give 200

https://docs.python.org/3/tutorial/inputoutput.html
"""


# inherit from Exception
class NotEnoughBalance(Exception):  #Inheriting from exception
    pass  # pass means no operation


class BankAccount:
    def __init__(self, initAmount):  # 1 methods, 2 arguments
        self.amount = initAmount  # instance variable, any method can update and access in this class

    # a = 0 #Simple var, scope is only this method

    def __str__(self):  # 1 special / internal methods #lots of the special methods have
        return f"BankAccount ({self.amount})"

    def transact(self, amount):  # 1 public / external methods
        if self.amount + amount < 0:
            raise NotEnoughBalance("Not possible")
        self.amount += amount


class BankUser:
    def __init__(self, name, initAmount):
        self.name = name
        self.account = BankAccount(initAmount)

    def __str__(self):
        return f"BankUser({self.name},{self.account})"

    def transact(self, amount):
        try:
            self.account.transact(amount)
        except NotEnoughBalance as ex:
            print(self.name, str(ex), amount)


# There are three bankusers
class NormalUser(BankUser):  #normal user inherits from Bank user
    pass


class GoldUser(BankUser):
    pass


class SilverUser(BankUser):
    pass


if __name__ == '__main__':  # This is module context
    users = [GoldUser("Gold", 100),
             SilverUser("Silver", 100),
             NormalUser("Normal", 100)]
    amounts = [100, -200, 300, -400, 400]
    for user in users:
        for am in amounts:
            user.transact(am)
        print(user)
