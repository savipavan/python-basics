'''
range function generate sequence of numbers
for loop use range function

for iterating_var in sequence:
    statements
'''

# basic for loop
for letter in "python":
    print('current letter: ', letter)

# Using range objects
# range parameter: start(inclusive), end(exclusive), step value
# observe '0' will not be printed

for i in range(10,0,-1):
    if i == 4:
        break
    elif i == 9:
        continue
    print(i)
# else block executes if loop terminates normally
# will not execute if exited due to break statement
else:
    print('Executes if loop terminates normally')
print("Loop ended")

# Examples of Ranges
for n in range(10):
    print(n, " ", end="")
print()

for c in "Hello":
    print(c, " ", end="")
print()

# Print first 5 numbers that are multiple of 7
print("First few numbers that are multiples")
num = 7
how_many = 5
# Range with a step
for n in range(num, num*how_many+1, num):
    print(n)
