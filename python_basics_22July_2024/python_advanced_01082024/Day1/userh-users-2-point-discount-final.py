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

Python everything is class
OOP:
    no access control(this means everything public no private)
    it have instance variable
        method - first arg is instance

    class variable(which is equalent to Java static)
        method - first arg is class
        can not access any instance variable
        can only access class variable

    it have intance method
    it have variable method
    static method
        there is no first arg
        generally used for NS

    property(like Java Beans)
    no abstract keyword
    no interface but has Abstract class, implemented metaclass
    it have concept of Metaclass : metaclass is a class which creates other classes
         metaclass is a class which creates other classes
        type is default metaclass
        Metaprogramming
            inherits from type and does
            class creation level manipulation
    slots etc - refer book called Learning Python - Mark Lutz(consider as Bibel) of python

    without decorator we cannot create class variable

    class method first argument is class, static method doesnt have first argument.
    in real life static method will not used

"""
DEBUG = False


def d_print(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


# inherit from Exception
class NotEnoughBalance(Exception):
    pass


class BankAccount:
    def __init__(self, initAmount):  #special method 1
        d_print("BankAccount.__init__")
        self.amount = initAmount  #instance variable, any method can update and access in this class
        #a = 0                       #simple var, scope is only this method

    def __str__(self):  #special method 2
        d_print("BankAccount.__str__")
        return f"BankAccount({self.amount})"

    def transact(self, amount):  #3 # public method
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


if __name__ == '__main__':  #?
    users = [GoldUser("Gold", 100),
             SilverUser("Silver", 100),
             NormalUser("Normal", 100)]
    amounts = [100, -200, 300, -400, 400]
    for user in users:
        for am in amounts:
            d_print(user, "for", am)
            user.transact(am)
        print(user)

    #ba = BankUser("abc", 100)   #BankUser.__init__( ba,"abc", 100)
    #ba.transact(100)
    #print(ba)               #BankUser.__str__(ba)       #BankAccount(200)
"""  
BankUser.__init__       GoldUser("Gold", 100)
BankUser.__init__       SilverUser("Silver", 100)
BankUser.__init__       NormalUser("Normal", 100)
BankUser.__str__        print(user, "for", am)
GOLD: BankUser(Gold, BankAccount(100)) for 100 print(user, "for", am)
GOLD: BankUser.transact                user.transact(am)
GOLD: BankUser.__str__                  print(user, "for", am)
GOLD: BankUser(Gold, BankAccount(200)) for -200 print(user, "for", am)
GOLD: BankUser.transact                user.transact(am) 
GOLD: BankUser.__str__
GOLD: BankUser(Gold, BankAccount(0)) for 300
GOLD: BankUser.transact
GOLD: BankUser.__str__
GOLD: BankUser(Gold, BankAccount(300)) for -400
GOLD: BankUser.transact
GOLD: Gold not possible -400
GOLD: BankUser.__str__
GOLD: BankUser(Gold, BankAccount(300)) for 400
BankUser.transact
BankUser.__str__
BankUser(Silver, BankAccount(100)) for 100
BankUser.transact
BankUser.__str__
BankUser(Silver, BankAccount(200)) for -200
BankUser.transact
BankUser.__str__
BankUser(Silver, BankAccount(0)) for 300
BankUser.transact
BankUser.__str__
BankUser(Silver, BankAccount(300)) for -400
BankUser.transact
Silver not possible -400
BankUser.__str__
BankUser(Silver, BankAccount(300)) for 400
BankUser.transact
BankUser.__str__
BankUser(Normal, BankAccount(100)) for 100
BankUser.transact
BankUser.__str__
BankUser(Normal, BankAccount(200)) for -200
BankUser.transact
BankUser.__str__
BankUser(Normal, BankAccount(0)) for 300
BankUser.transact
BankUser.__str__
BankUser(Normal, BankAccount(300)) for -400
BankUser.transact
Normal not possible -400
BankUser.__str__
BankUser(Normal, BankAccount(300)) for 400
BankUser.transact 


######################PROMPT
>>> class A:
    ...     pass
...
>>> class B(A):
    ...     pass
...
>>> class C(A):
    ...     pass
...
>>> class D(B,C):
    ...     pass
...
>>> d = D()
>>> D.__init__(d)
>>> d.any_var
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'D' object has no attribute 'any_var'
>>> #Method resolution order - MRO
>>> #using internal attributes
>>> d.__class__
<class '__main__.D'>
>>> d.__class__.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
>>> #class object is root of any class
>>> dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> A.any_var = 20
>>> d.any_var # 0/20/error
20
>>> D.any_var = 200
>>> d.any_var
200
>>> B.any_var = "OK"
>>> d.any_var
200
>>>
"""
