# input
age = int(input("Enter your age:"))
print(age)
print(type(age))
# by default all values in input function is string

# convert input values from string to int
name = input("Enter your name:")
print(name)
print(type(name))

# convert input value from string to float
num = float(input("Enter your number:"))
print(num)
print(type(num))

# convert variable type to str
a = 5
print(type(a))
print(str(a))
print(type(str(a)))

# len to find out the lenght of the string
course = "python"
print(len(course))

### Formatting output with print()
a = 10
b = 20

# The value of a is 10 and b is 20
print("The value of a is {} and b is {}".format(a,b))

print("I love {} and {}".format("apples","oranges"))
print("I love {1} and {0}".format("apples","oranges"))
print("I love {second} and {first}".format(first="apples",second="oranges"))

## formating decimal
x = 33.852984218515245
print("The value of x is %6.4f" % x) # total 6 digits and 4 digits after dot
print("The value of x is %4.2f" % x)
print("The value of x is %2.1f" % x)

