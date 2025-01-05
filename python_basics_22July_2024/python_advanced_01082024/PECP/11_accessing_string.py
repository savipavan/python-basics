'''
Accessing string
- using index
- Using slice operator
'''

a = "python"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print("--------------")
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

print("length of the string")
print(len(a))

print("While-loop to get length of the string")
i = 0
length = len(a)
while i < length:
    print(a[i])
    i = i + 1

####################3
# String slicing
a = "Python"
# string_name[start_index: end_index: step]
print(a[1:4:1])
print(a[1:4:2])
print(a[1:4:1])
print(a[1:4:]) # remove step
print(a[1::]) # remove start_index
print(a[:4:]) # remove start_index
print(a[:4:2])


### operations on strings
# two operations can be carried, addition and multiplication
s1 = "python"
s2 = "programming"

# Addition(+)
a = s1 + s2
print(a)

# multiplication / repetation(*)
b = s1 * 2 #repeated twice
b = s1 * 3 #repeated thrice
print(b)


#######################
# Operator precedence in python

'''
Paranthesis ()
Exponential operator    **
Biwise complement operator, Unary minus operator, unary plus operator
muliplication, division, modulo, floor operation
Addition, Subtraction
Bitwise shift operator
'''


