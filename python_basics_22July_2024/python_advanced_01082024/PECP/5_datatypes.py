# Data types
'''
1-Sequence
    a=String
    b=List
    c=Tuple
2-Set
3-Boolean
4-Dictionary
5-Number
    a=Integer
    b=Complex
    c=Float
'''
# Integer type
a = 10
print(type(a))

#Float
b = 2.5
print(type(b))
c = 2e3
print(type(c))
print(c)

# Complex numbers
# x + yj
a = 10 + 11j
print(a)
print(type(a))

'''
# sep stands for seperator
# end
'''

# sep
a = 10
b = 20
c = 30

print(a,b,c)
print(a,b,c, sep=",")
print(a,b,c, sep="")
print(a,b,c, sep=":")
print(a,b,c, sep="/n")

# end will be used when output is on the same line
print("I love python")
print("Yes")

print("I love python", end="")
print("Yes")

print("I love python", end=".")
print("Welcome")

#end,sep togther
print("Monday", "Tuesday","Wednesday", sep=',')
print("Thursday", "Friday","Saturday", sep=',')

# print in single line by adding end
print("Monday", "Tuesday","Wednesday", sep=',', end=",")
print("Thursday", "Friday","Saturday", sep=',')


