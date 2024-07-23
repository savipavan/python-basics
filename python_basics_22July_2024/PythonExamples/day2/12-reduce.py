# Reduce
from functools import reduce

input_list = range(1,15)
print(list(input_list))
print(reduce(lambda x, y: x+y, input_list))

# determing the maximum of a list of numerical values by using reduce
from functools import reduce
f = lambda a,b: a if (a > b) else b
maxnum = reduce(f, [47,11,42,102,13])
print(maxnum)