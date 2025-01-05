# Binary to decimal
#0000 0101

#Decimal to binary
# need to divide number by 2

'''
- Left shift operator(<<)
- Right shift operator(>>)
- Bitwise complement operator(~)
'''

# Left shift operator(<<)
a = 5
# Left shift operator
print(a<<1)
print(a<<2)

# Right shift operator
print(a>>1)
print(a>>2)

#Bitwise complement operator
print(~10)
print(~-5)


### Boolean operators or logical operators
# and
print("Logical and")
print(True and False)
print(True and True)

# and also works with integers, (X and Y) -->
# if X is false then the result is x otherwise the result is y
print(0 and 10) # because is x false hence it prints 0
print(10 and 20) # result is 20 as x is true and will display 20

# and also workds with Strings, if any of the argument is blank then
# you will get blank as the output
# if both the argument are having string values then the result with the second string value

print("python" and "java")
print("" and "java") #empty string will be printed


# or
# logical or
print("Logical OR")
print(True or False)
print(False or False)

# or also works with integers(x or y) -->
# if x is true then the result is x else the result is false
print(0 or 10)
print(20 or 10)

# or also works with Strings, First argument will be the output always if it's not blank.
# if blank, output is the second argument.
print("Python" or "")
print("Python" or "Java")
print("" or "Java")

# not
# logical not
# if it false then it result true if it is true then it return false
print("LOGICAL NOT")
print(not True)
print(not False)

# Not can also be used with Integers,
# it will return True if used with 0 else it will return false
print(not 10)
print(not 100)
print(not 0)

# not can also be used with Strings, it will return True if the string is empty,
# it will return false if string is not empty
print(not "")
print(not "python")

# comparision operators
# ==
print("COMPARISION OPERATORS")
print(10 == 20)
print(10 == 10)
a, b = 10, 15
print(a == b)

# !=
print(10 != 20)
print(10 != 10)
a, b = 10, 15
print(a != b)

# >
print(10 > 1)
print(10 > 100)
print(10 > 10)

# <

print(10 < 1)
print(10 < 100)
print(10 < 10)

# >=
print(10 >= 10)
print(10 >= 100)
print(1000 >= 10)

# <=
print(10 <= 10)
print(10 <= 100)
print(1000 <= 10)


