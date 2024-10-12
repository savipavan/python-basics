**** Python Advanced workshop ****

1-Aug-2024 (10am to 6pm)


    ** Instructor name: 
        Nirmalya Das, mail: ndas1971@gmail.com

    **Recommended Book:
           Core Python:Learning Python, Mark Lutz 
           Adv Python: Programming python, Mark Lutz
    
   
    ** How to get data for workshop - Store them in your local directory
           iris.csv
           example.xml
           example.json
           example1.xml
       
    ** If you don't have anaconda, install below in command prompt or in devshell
            pip install poetry pytest pytest-cov requests  beautifulsoup4 flask sqlalchemy numpy  pandas  openpyxl xlrd matplotlib wheel gevent
    
    
    ** Daily Quiz:    
    please Use same browser and same user name for all days

    Day1 Quiz:  https://bit.ly/4bTDwJR
           
    DAY2 Quiz: https://bit.ly/4bRnmR8

    **  Check your quiz result at:    
    (Use the same browser where quiz is submitted)
    https://bit.ly/3XkqWPj


############################################################################################
D:\>mkdir handson

D:\>cd handson

D:\handson>echo > userh.py

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
if __name__ == '__main__':          #?
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
"""

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
>>>
>>> class A:
...     def __init__(self):
...             self.instance_var = 0
...     def instance_method(self):
...             return 2
...
>>> #instance variable/method is given above
>>> a = A()
>>> a.instance_var
0
>>> a.instance_method()
2
>>> #class method - first arg is class not instance
>>> class A:
...     class_var = 0
...     @classmethod
...     def meth(cls):
...             print(cls)
...             return 3
...
>>> A.class_var
0
>>> A.meth()
<class '__main__.A'>
3
>>> #@ is decorator
>>> #class var is actaully global for all the instances of class
>>> class B(A):
...     pass
...
>>> B.class_var
0
>>> #static method - @staticmethod, and there is no first argument
>>> class A:
...     @staticmethod
...     def p():
...             return 4
...
>>> A.p()
4
>>>

###################test_userh.py
"""
Execute
pytest -v test_userh.py

With coverage
pytest  --cov=userh --cov-report term-missing test_userh.py


"""
"""
https://docs.pytest.org/en/6.2.x/assert.html
Testing exception etc
https://docs.pytest.org/en/6.2.x/fixture.html
test data , setup and teardown
https://docs.pytest.org/en/6.2.x/capture.html
capture stdout and stderr
https://docs.pytest.org/en/6.2.x/skipping.html
skipping based on condition
filtering test case
https://docs.pytest.org/en/6.2.x/usage.html
command line usage
https://docs.pytest.org/en/6.2.x/monkeypatch.html
mock testing

Filtering testcase
Usage mark
Using K expr
-k EXPRESSION         Only run tests which match the given substring expression. An
expression is a Python evaluatable expression where all names are
substring-matched against test names and their parent classes.
Example: -k 'test_method or test_other' matches all test functions
and classes whose name contains 'test_method' or 'test_other', while
-k 'not test_method' matches those that don't contain 'test_method'
in their names. -k 'not test_method and not test_other' will
eliminate the matches. Additionally keywords are matched to classes
and functions containing extra names in their 'extra_keyword_matches'
set, as well as functions which have names assigned directly to them.
The matching is case-insensitive.
# Run only silver case
pytest -v -k "Silver" test_userh.py
#Run only silver and gold case
pytest -v -k "Silver or Gold" test_userh.py
#Run all from TestUser suite
pytest -v -k "TestUser" test_userh.py
#Run all except TestUSer
pytest -v -k "not TestUser" test_userh.py

"""
from userh import *
#Testcase - fn starting with test
#module name starting with test
#all test modules are in tests/
#test suite is a class starting with Test


class TestUser:
def test_normal_user(self):
u = NormalUser("Normal", 100)
amounts = [100, -200, 300, -400, 400]
for am in amounts :
u.transact(am)
assert u.account.amount == 700         
def test_Gold_user(self):
u = GoldUser("Normal", 100)
amounts = [100, -200, 300, -400, 400]
for am in amounts :
u.transact(am)
assert u.account.amount == 710     
def test_Silver_user(self):
u = SilverUser("Normal", 100)
amounts = [100, -200, 300, -400, 400]
for am in amounts :
u.transact(am)
assert u.account.amount == 706

def test_ba_str():
ba = BankAccount(100)
assert str(ba) == "BankAccount(100)"
########################
if __name__ == '__main__':   # pragma: no cover   
