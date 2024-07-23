'''
Set is a mutable collection of items
we can add, update and delete set elements once it is initialized
items in the set, do not have any index
each time you run your code, items would be in different order
we annot have duplicate elements in the set
when existance of the item is important, not the order of the item - go with set
'''
import numbers

# basic set creation using {} braces
Days = {"Monday", "Tuesday", "webnesday", "Thursday", "Friday"}
print(Days)
print(type(Days))
print("looping through the set elements ...")
for i in Days:
    print(i)

# Sets creation using set() method
empty_set = set()
empty_set.add(234)
print(empty_set)

emps = ['p12', 'e34', 'p17', 'p19']
emps_set = set(emps)

# search for exsistance of an element
print('p12' in emps_set)

# Does not support indexing
# print (emps_set[0])

# convert a set to list and use indexing
emp_list = list(emps_set)
print(emp_list[2])

numbers = (23, 553, 79, 91, 13, 7)
odds_nums = (23, 553, 79, 91, 13, 7)

# Add multiple elements (from a list/tuple/set) to a set
numbers.update(odds_nums)
print(numbers)

# Remove an element
numbers.remove(553)
print(numbers)

# copy of the set
n1 = numbers.copy()
print(n1)

# remove the first element
print(numbers.pop())

# empty the set
numbers.clear()
print(numbers)