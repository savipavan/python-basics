# Tuple is an immutable collection of items
# You cannot modify the tuple elements once the tuple is initialized each item in the typle has index list list
# each item in the tuple is, separated like list
# it is like a read-only list
# In python, each, separated items is considered as tuple

'''
below are teh valid tuples
employee = "pavan, "kumar", "venkata"
employee = ("pavan, "kumar", "venkata")
print(*args,sep='',end="\n")

# when we want readonly data we use tuple
'''

# Tuples
empty_tuple = ()
emp_ids = 'p873874', 'E948573','P24875', 46

# print object types
print(type(empty_tuple))
print(type(emp_ids))
print(type(emp_ids[1]) is int)
print(type(emp_ids[1]) is str)
print(emp_ids)

# use tuple constuctor to create a tuple of letters
# tuple constructor takes only one value
name_tuple = tuple("Krunal Trivedi")
print(type(name_tuple))
print(name_tuple)

# to create tuple of one string value
names = "pavan kumar venkata" # remove the comma at the end and see
print(type(names))
print(names)

# try to modify a tuple
# empty_tuple[0] = "my python"

# list
names_list = ["john", "mike", "pat", "bob", "bill"]
print((type(names_list)))

# create a tuple from a list
empty_tuple = tuple(names_list) + name_tuple
print(empty_tuple)

# print tuple contents
print('Contents of tuple created from list: ')
for el in empty_tuple:
    print(el)

print("Contents of Emp_IDs tuple: ")
print(emp_ids)

print(emp_ids.index("P284726"))
print(name_tuple.count('h'))
print(len(empty_tuple))
print(max(name_tuple))
