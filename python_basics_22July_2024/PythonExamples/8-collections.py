# Work with collection: Python Data Structure
'''
1 - list : List is mutable collection of items
We can add, update and delete items once the list is initialized

2 - tuple
each item in the list is , seperated
each item in the list has an index, starting with 0
[]
["Venkata", "pavan", "Kumar"]

list() - it converts another type of data structure to list


3 - Set
4 - Dictionary
'''

my_empty_list = []
print('empty list: {}, type: {}'.format(my_empty_list, type(my_empty_list)))

# This is how we can create list
list_of_ints = [1,2,6,7]
list_of_misc = [0.2, 5, 'Python', 'is', 'still fun', '!']
print('length: {} and {} '.format(len(list_of_ints), len(list_of_misc)))
intSeq = list(range(1,10))
print(intSeq)
print(list(range(10)))

# access and modify element
intSeq[2] = 111
print("Elements of intSeq after modification: ", intSeq)

# the '*' operator works as a repetition operator on strings
print("List repetion:")
print(list_of_ints * 3)

# the '*' operator workds as multiplication operator on numeric values
print(list_of_misc[1]* 3)

# 2 -dimensional list
coordinates = [[1,2], [3,4], [5,6], [7,8]] # two dimensional
print('first coordinate: {}'.format(coordinates[0]))
print('second element of the first coordinate: {}'.format(coordinates[0][1]))
print('first element of the first coordinate: {}'.format(coordinates[0][0]))

# 3 dimensional list
threeDList = [[1,2,3,[10,20,30]], ['A','B','C']]
print(threeDList [0][3][1]) # Guess the output
print(threeDList[1][2])

# remove element we can use del keyword using index
del intSeq[0]
print(intSeq)

# Checking if certain value is present in the list
languages = ['java', 'c++', 'Go', 'Python', 'JavaScript']
if 'Python' in languages:
    print('Python is in the list of languages')

if 6 not in [1,2,3,4,5]:
    print('6 is not in the list')

# List concatenation
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print('list1 : {}, list2 : {}, list3 : {}'.format(list1, list2, list3))

# List are mutable
original = [1,2,3]
modified = original
modified[0] = 99
print('original : {}, modified : {}'.format(original, modified))

# copy() method creates the new list
original = [1,2,3]
modified = original.copy()
modified[0] = 99
print('original-modified : {}, modified : {}'.format(original, modified))

# list.append()
my_list = [1]
my_list.append('ham')
print(my_list)

my_list.insert(0, 'Python')
print(my_list)

my_list.insert(3, 12)
print("After element inserted: ", my_list)

# List.remove
my_list = ['Python', 'is', 'sometimes', 'fun']
print(my_list)
my_list.remove('sometimes')
print(my_list)

# if we are not sure that the value in the list, better to check
if 'Java' in my_list:
    my_list.remove('Java')
else:
    print('Java is not in the list')
print(my_list)

# del remove item based on index
# remove keyword based on value

# List sort method
# use list.sort() method to sort a list inplace
# sorts elements of original list
numbers = [8,1,6,5,10]
numbers.sort()
print("Sorted list: ", numbers)

# sort in revert order
numbers.sort(reverse=True)
print('numbers reversed: {}'.format(numbers))

words = ['this', 'is', 'a', 'list', 'of', 'words']
words.sort()
print('words: {}'.format(words))

# Sorted function
# sorted(list) method returns the new list and leaves the original
numbers = [8, 1, 6, 5, 10]
sorted_numbers = sorted(numbers)
print('numbers: {}, sorted: {}'.format(numbers, sorted_numbers))

# List. extend()
# use list.extend() method to add items from another list
first_list = ['beef','ham']
second_list = ['potatoes', 1, 3]
first_list.extend(second_list)
print('first: {}, second: {}'.format(first_list, second_list))

# list. reverse()
# use list.reverse() method to reverse the order of a list
numbers = [1,2,3,4,5,6,7,8,9]
numbers.reverse()
print('numbers reversed: {}'.format(numbers))

# list comprehensions
l = [letter for letter in "This is character]"]
print(l)

# create a list of elements using expression
evenList = [i*2 for i in range(10)]
print(evenList)

# extract only even numbers from a list using list comprehension
nums = [23, 456, 56, 213, 5, 24, 82, 983, 34]
even_nums = [number for number in nums if number % 2 == 0]
print("Even numbers extracted: ", even_nums)

# square of numebers
l = [num ** 2 for num in range(11)]
print("Squares: ", l)

# nested list comprehensions
l = [n * 2 for n in [num ** 2 for num in range(11)]]
print(l)