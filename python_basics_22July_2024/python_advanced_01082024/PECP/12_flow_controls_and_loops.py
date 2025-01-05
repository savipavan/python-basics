''''
Flow controls are 3 types:
    - Conditional
        - if
        - else
        - elif
    - Transfer
        - break
        - continue
        - pass
    - Iterative
        - for
        - while
'''

######## if-else
'''
# if statement
Syntax of if statement in java
if condition:
    code to be executed:
'''
#age = int(input("enter age: "))
age = 21
if age > 18:
    print("you are welcome")

'''
if else statement

Syntax of if statement in java
if condition:
    code to be executed
else:
    code to be executed
'''

# if-else statement
if age > 18:
    print("You are welcome")
else:
    print("you below 18, can't enter")

## Coding excersize # Write a program to accept 2 numbers from user and print the largest
#a = int(input("Enter first number: "))
a = 10
b = 20
# b = int(input("Enter second number: "))
if a > b:
    print("{} is big number".format(a))
else:
    print("{} is big number".format(b))


''''
elif statement or nested if statement

if condition:
    code will be executed
elif condition:
    code will be executed
else:
    code will be executed
'''
a = 0
if a > 0:
    print("positive")
elif a == 0:
    print("zero")
else:
    print("negative")

'''
Nested if statement
'''
age = 61
if age > 18:
    if age > 60:
        print("you will get senior citizen account")
    else:
        print("you will get savings account")
else:
    print("you are not eligible")

'''
Coding challenge: Write a program to accept 3 numbers from user and print the largest
'''
#a = int(input("enter a first number: "))
a = 10
#b = int(input("enter b second number: "))
b = 15
#c = int(input("enter c third number: "))
c = 20

if a > b and a > c:
    print("a is gretest")
elif b > a and b > c:
    print("b is gretest")
elif c > a and c > b:
    print("c is gretest")


'''
for loop in python
for x in sequence:
    code will be executed
'''
# a = "I love python"
# for x in a:
#     print(x)
#
# # generate numbers with step of 2
# for i in range(1,10,2):
#     print(i)

'''
for loop with if else statement
'''
#
# for i in range(1,10,2):
#     if i == 5:
#         print("number is less than 5")
# else:
#     print("No entry found")

'''
Coding challenge: Write a program to display even numbers from 0 to 20
'''
# for i in range(0,20,2):
#     print(i)

'''
while loop
# loop helpful if computer to do until satisfy condition

while condition:
    body
    
# some notes
- While loop is generally used when you are not aware of the number of iterations upfront
- while loop is executed till condition specified returns false
- body of while loop is determined by the indentation
- you can use non boolean value in place of condition,any non zero value will be treated as true and 0 will be treated as false    
'''

a = 1
while a < 5:
    print(a)
    a = a + 1
print("Outside while")

'''
Coding challenge: Write a program to display sum of n numbers
'''
#a = int(input("Enter a number: "))
a = 5
sum = i = 0
while i <= a:
    sum = sum + i
    i = i + 1
print(sum)


'''
break statement
break statement to exit loop, when certain condition is encounter
'''
a = 5
while a:
    print(a)
    a = a - 1
    if a == 3:
        break
print("Outside while loop")


a = 5
while a:
    print(a)
    a = a - 1
    if a == 3:
        break
    print("inside while loop")
print("Outside while loop")

a = [1,2,3,4,5]
for x in a:
    print(x)
    if x == 3:
        break
print("outside for loop")

'''
Continue statement
'''
a = 5
while a:
    print(a)
    a = a - 1
    print("End of the loop")

a = 5
while a:
    print(a)
    a = a - 1
    if a == 3:
        continue
    print("End of the loop")

# break exist the loop
# continue evaluate the condition and iterate

'''
pass statement
'''
a = 1
while a < 10:
    print("hello")
    a = a + 1

a = 1
while a < 10:
    pass
