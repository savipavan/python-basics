num1, oper, num2 = input("Enter operation to perform ").split()

# convert input value to integer
# fails if input is float value
num1 = int(num1)
num2 = int(num2)

print(num1)
print(num2)

# Do the arithemic opertions based on operation
# +, -, *, /

if oper == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif oper == '-':
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif oper == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif oper == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print("Enter one of the +, - , *, / operator.")