PyTest - Testing the code

** If you don't have anaconda, install below in command prompt or in devshell
pip install poetry pytest pytest-cov requests  beautifulsoup4 flask sqlalchemy numpy  pandas  openpyxl xlrd matplotlib wheel gevent


https://wiki.python.org/moin/PythonTestingToolsTaxonomy

PyTest is third party module by installing through pip
check pytest installed or not?

pytest --version

#Testcase - fn starting with test
# module name starting with test
# all test modules are in tests/
# test suite is a class starting with test
'''
execute pytest -v tesst_userh.py

with coverage
pytest -v --cov=userh --cov-report term-missing test_userh.py

'''

# Unit test coverage is 98%
 # with coverage
pytest --cov=userh --cov-report term-missing test-userh.py

(venv) PS C:\Users\varri\IdeaProjects\python-basics\python_basics_22July_2024\python_advanced_01082024\Testing> pytest --cov=userh --cov-report term-missing test_userh.py


test_userh.py ...                                                                                                                                                                                                            [100%]

---------- coverage: platform win32, python 3.12.3-final-0 -----------
Name       Stmts   Miss  Cover   Missing
----------------------------------------
userh.py      53     12    77%   58, 70-71, 88-89, 117-125
----------------------------------------
TOTAL         53     12    77%

line no 58 is not coverage
69-70 is not covered

**********

https://docs.pytest.org/en/6.2.x/contents.html
https://docs.pytest.org/en/6.2.x/assert.html
    Testing exception etc
https://docs.pytest.org/en/6.2.x/fixture.html
    Test data, setup and teardown
https://docs.pytest.org/en/6.2.x/capture.html
    how to capture stdout and stderr
https://docs.pytest.org/en/6.2.x/skipping.html
    skipping based on condition(some tests are based on linux, some are in windows)
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

    # Testcase name
    test_userh.py::TestUser::test_normal_user PASSED                                                                                                                                                                             [ 33%]
    test_userh.py::TestUser::test_gold_user PASSED                                                                                                                                                                               [ 66%]
    test_userh.py::TestUser::test_silver_user PASSED
    test_userh.py::test_ba_str PASSED

********

# Function can be an argument of another function
def p(x):
    return lambda y: x+y

>>> def p(x):
...     return lambda y: x+y
...
>>> p(2)(3)
5
>>> type(p(2))
<class 'function'>
>>> type(p(2)(3)
... )
<class 'int'>
>>> # Function be be also return value of another function
>>> # function name is a variable
>>> # function can take another function as arg or return another function