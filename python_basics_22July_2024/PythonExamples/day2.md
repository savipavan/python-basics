# custom function

Types of argument
- required argument
- default argement
- keyword argument
- variable length argument(lenght of the argument wont fixed)


# Variable Scope
- location of the variable where we declare and usage
- scope of variable
  - no scope - available in it's own frame
  - local - variable define inside the function block
  - global - variable define outside the function

# Lambda function: function without name small anonymous function used to perform inline login
lambda list of arguments: expression

it is heavily used in map(), filter(), reduce()

# for loop
for item in list1:
  list2.append(item**2)

(or)
# List comprehension
list1 = item*2 item in list1

# math function
map() function applies given logic on each item of collection and return map object
map(logic, collection)
map(lambda x:x**2, list1)

## Filter() method
filter() applies given logic on each item of the collection but it returns only filtered value -- value which tested true in the logic

filter(logic, collection)
filter(lambda x: x%2 = 0, list1)

# reduce function:
reduce() applies given logic on each item on collection and returns a single calculated value

## file IO

# tell() and seek()

