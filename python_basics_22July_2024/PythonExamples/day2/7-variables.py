# Variable scope demo
total = 0  # This is global variable


# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them.
    total = arg1 + arg2  # here total is local variable.
    print("Inside the function local total: ", total)  #30
    return total


# Now you can call sum function
sum(10, 20)
print("Outside the function global total : ", total)  #0