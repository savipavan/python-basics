# Keyword Arguments
def my_fancy_cal(first, second, third):
    return first + second + third

print(my_fancy_cal(3, 2, 1))
print(my_fancy_cal(first=3, second=3, third=2))

# with keyword arguments you can mix the order
print(my_fancy_cal(third=4, first=2, second=1))

# you can mix arguments and keyword arguments but you have to start with arguments
print(my_fancy_cal(3, third=1, second=2))