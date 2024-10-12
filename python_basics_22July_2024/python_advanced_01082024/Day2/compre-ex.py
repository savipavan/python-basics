# Map pattern - Process each element
lst = [2, 4, 7, 9]

# Square of reach number
# we need to question our self whether we need to give output in list, dict or map
## this comprehension works for multiple operations

o = []
for e in lst:
    o.append(e * e)
print(o)

## writing the same above code in below
# equiv - list compre
o = [e * e for e in lst]
print(o)

# set compre - set - unique
o = {e * e for e in lst}
print(o)

# dict compre - dict - k:v pairs
o = {e: e * e for e in lst}
print(o)

#Square only even nos
o = []
for e in lst:
    if e%2 ==0:
        o.append( e*e)
print(o)
#Square only even nos -in comprehension
o = [e * e for e in lst if e % 2 == 0]
print(o)

# Create a pair of even and odd number - Nested for loop

o = []
for e in lst:
    if e%2 ==0:
        for e1 in lst:
            if e1 % 2 ==1:
                o.append((e, e1))
print(o)

# Set compare - set unique - can have filter, multiple for etc
o = [ (e, e1) for e in lst if e % 2 == 0
              for e1 in lst if e1 % 2 == 1]
print(o)