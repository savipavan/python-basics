'''
What are functions:
- Collections of python statements to perform an operation.
- Functions make your code modular,organized,manageable,reusable.

Syntax:
def function_name(parameters):
    statement(s)
'''


# python functions

def print_hello():
    print("hello world")


print_hello()

## Function arguments and parameter
# want to print name
# One parameter function
def print_hello(name):
    print("hello", name)

print_hello("python")
print_hello(12)

# mulitiple parameter function
def print_hello(greeting, name):
    print(greeting, name)

print_hello("Hi","python")
print_hello(12,14)

# mulitiple parameter with user input
def print_hello(greeting, name):
    print(greeting, name)

print_hello("Hi",input("enter name: "))

