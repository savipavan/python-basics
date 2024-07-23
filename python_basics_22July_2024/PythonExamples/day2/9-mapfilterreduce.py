def square(num):
    return num * 2

input_list = range(1,11)

# arthmetics operations can't be performed directly on lists or range objects
# print(list(input_list) * 2) # performs list repetition but not multiplication
# print(list(input_list) ** 2) # can't perform

m1 = map(square, input_list) # returns a map object
print(m1)
print(list(m1))

# Pass lambda expressions in place of function
print(list(map((lambda x:x ** 2), input_list)))

# Passing multiple iterators
num1 = [4,5,6]
num2 = [5,6,7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))