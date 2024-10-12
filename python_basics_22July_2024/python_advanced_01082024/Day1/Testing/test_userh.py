"""
Execute
pytest -v test_userh.py

With coverage
pytest -v --cov=userh --cov-report term-missing test_userh.py


"""
from userh import *

#Testcase - fn starting with test
#module name starting with test
#all test modules are in tests/
#test suite is a class startig with Test

class TestUser:
    def test_normal_user(self):  #Instance method
        u = NormalUser("Normal", 100)  #question how is the NormalUser got the value
        amounts = [100, -200, 300, -400, 400]
        for am in amounts:
            u.transact(am)
        assert u.account.amount == 700  #assert is checking the value

    def test_gold_user(self):
        u = GoldUser("Gold", 100)  #question how is the NormalUser got the value
        amounts = [100, -200, 300, -400, 400]
        for am in amounts:
            u.transact(am)
        assert u.account.amount == 710  #assert is checking the value

    def test_silver_user(self):
        u = SilverUser("Silver", 100)  #question how is the NormalUser got the value
        amounts = [100, -200, 300, -400, 400]
        for am in amounts:
            u.transact(am)
        assert u.account.amount == 706  #assert is checking the value

def test_ba_str():
    ba = BankAccount(100)
    assert str(ba) == "BankAccount(100)"