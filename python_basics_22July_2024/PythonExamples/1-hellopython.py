my_int = 6
print(my_int)

print(type(my_int))


my_float = float(my_int)
print(my_float)
print(type(my_float))

print(1/1)
print(6/5)

# modulus %, power **
print(7%5)
print(2**3)

## meta programming
my_int = my_int + my_int
print(my_int)

# Multiple assigment - single value to multiple values
x = y = z = 50
print(x)
print(y)
print(z)

# multiple assignments - assigning multiple values
p,q,r = 5,10,15
print(p)
print(q)
print(r)

# Multiple string with the backslash at the end of the each line
test = 'Hello\
        python\
        you\
        dynamic'

print(test)

# multiple string with triple quotes

test1 = ''' welcome
to the 
office'''
print(test1)

print(len(test1))

## You cannot concate with string with integer
age = 18
name = 'pavan'
#print(name+ 'is' + age + 'years old')
print(name,'is',age,'years old')
print(name+ ' is ' + str(age) + ' years old ') # converting integer to string
print("{0} is {1} years old".format(name,age)) # str.format() it is pythong recommended approach
print('%s is %d years old' %(name, age)) # %s - String, %d - Integer

# str.firmat()
# using format option in a simple string
print("{}, A computer science portal for geeks.".format("Stackoverflow"))

# using format option for a value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old!".format(18))



## Python program demonstrating index error
# number of placeholders are four but there are only three values passed
# parameters in format function

my_string = "{}, is a {} science portal for {}"
print(my_string.format("Stackoverflow", "computer", "geeks."))