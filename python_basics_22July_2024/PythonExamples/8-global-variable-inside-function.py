# Global scope example
# global variable can be accessed inside or outside of the function
total = 0
def sum(arg1, arg2):
    global total

    # Add both the parameters and return them.
    total = arg1 + arg2

    print("Inside the function local total : ", total) #30
    return total

# Now you can call sum function
sum(10, 20)
print("outside the function global total: ", total) #30