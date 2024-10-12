###################userh.py
# Bank User has name and account. There are two types of Users
# Normal and privileged user . There are two types of privileged
# users, Gold and Silver. Gold has cashback of 5% and Silver has
# cashback of 3% of expenditure when they spend any cash

"""
nouns
verbs"
    methods

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
"""


class BankAccount:
    def __init__(self, initAmount):  # 1 methods, 2 arguments
        self.amount = initAmount                # instance variable, any method can update and access in this class
        a = 0 #Simple var, scope is only this method

    def __str__(self):  # 1 special / internal methods #lots of the special methods have
        return f"BankAccount ({self.amount})"

    def transact(self, amount):  # 1 public / external methods
        self.amount += amount


if __name__ == '__main__':
    ba = BankAccount(100)   #each line corresponds to method. it initilize method  #BankAccount.__init__
    ba.transact(100)
    print(ba)  #BankAccount(200)    # What method it pics BankAccount.__str__(ba)
