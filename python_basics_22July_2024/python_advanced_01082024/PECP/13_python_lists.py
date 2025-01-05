'''
properties of list
    - Duplicate objects are allowed
    - insertion order is preserved

index as backbone:
    - allows you to differentiate between duplicate objects
    - preserves the insertion order of lists
'''

'''
Creating and accessing elements in lists
'''
# empty list
a = [] # empty list
print(a)
print(type(a))

# List with elements
a = [1,2,3,4,5,6]
print(a)
print(type(a))

# list with string with split()
s = "I love python"
a = s.split()
print(a)
print(type(a))

# Using list()
a = list(range(10,20,2))
print(a)
print(type(a))

# List of numbers
a = [1,2,3,4,5,6]

# list of strings
a = ["python","programming"]

# list of mixed data types
a = ['python',1,2,3,"name",2,"python"]
print(a)
print(type(a))

# Create a list within list(nested list)
a = [1,2,['a','b'],3,['c','d']]
print(a)
print(type(a))

# accessing elements of list
a = [1,2,3,4,5,6,7,8,9,10,11]
# using index
print(a[1])

# using slice operator
# print from 1st index to 10th index with step of 1
print(a[1:10:1])
# print from 1st index to 10th index with step of 2
print(a[1:10:2])

# print from 1st index to 10th index with step of 1
print(a[1:10])

# print from 1st index to 10th index with step of 2
print(a[1::2])

# prints from 1st index to 11th index with step of 2
print(a[1:500:2])

# prints reverse from 10th index to 1st index at step of -2
print(a[10:1:-2])

'''
updating elements in list

'''
a = [1,2,3,4,5,6,7,8,9,10,11]
# Adding new elements to list

# using index to change value
print(a)
a[1] = 100
print(a)

# using slicing operator to change values
a[1:4] = [33,34,35]
print(a)
# using append() function
a.append(200)
print(a)
a.append(300)
print(a)

a.append([2,40,50])
print(a)
# using extend() function
# append list to another list
a.extend([2,40,50])
print(a)

b = [9,99,999]
a.extend(b)
print(a)
# using insert() function
# insert function used to insert elements at given index
a.insert(2,1)
print(a)

# Deleting elements from the list
# using del function
del a[1]
print(a)

del a[1:3] # delete from range of values
print(a)

# using remove()
a.remove(5) #elements will be removed
print(a)

a.remove(99) # 99 element will be removed
print(a)

# we cannot use range from remove

# using pop()
#pop function expects index as parameter that item want to
# if n index provided then it will remove last item
a.pop(1)
print(a)

a.pop()
print(a)


# using clear()
# clears the all values from the given list
a.clear()
print(a)


''''
- important functions with list
'''
a = [1,2,3,4,5,6,7,8,9,10,11,1,1]
print(a)

# len()
print(len(a))

# count() # count function returns count of the given number in the list

print(a.count(1))

# index() # index gives the value of given index
print(a.index(1))

# sort() sort function arrange list in assending order
print(a.sort()) # we should not use this way
a.sort()
print(a)

#reverse of the given list
a.reverse()
print(a)

'''
Traversing through lists
'''
a = [1,2,3,4,5,6,7,8,9,10,11]
# Using while loop
i = 0
while i < len(a):
    print(a[i])
    i = i + 1

# Using for loop
print("Using for loop")
for x in a:
    print(x)

# Using range() function
print("using range function")
n = len(a)
for i in range(n):
    print(i,":",a[i])

a = 5/2
print(a)
print(type(a))

for i in range(2, 8, 2):
    print(i)


print("Python", "PCEP", sep="-", end="!")
print("Exam")

a = 7
b = 3

result = a & b
print(result)


def mystery_function(n):
    return n + sum(int(digit) for digit in str(n))

result = mystery_function(123)


x = [1, 2, 3]
y = x
y[0] = 10
print(x)

def multiply(a, b):
    if b == None:
        b = 3

    result = a * b
    return result

x = 5
y = None
output = multiply(x, y)
print(output)

######
x = 5
y = 2
result = x // y + x % y
print(result)
#####
x = 10
y = 3
z = x / y

result = round(z)

print(result)