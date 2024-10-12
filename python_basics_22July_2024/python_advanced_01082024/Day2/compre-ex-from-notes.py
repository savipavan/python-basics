############################################################################################
############compre_ex.py
#Map pattern - process each element
lst = [2,4,7,9]

#Square of each number
#list - insertion ordered, duplicates
o = []
for e in lst:
    o.append( e*e )

print(o)
#equiv - list compre
o = [ e*e for e in lst ]
print(o)
#square only even nos
o = []
for e in lst:
    if e%2 == 0:
        o.append( e*e )
#equiv
o = [ e*e for e in lst if e%2 == 0]
print(o)

#Create a pairs of even and odd number
o = []
for e in lst:
    if e%2 == 0:
        for e1 in lst:
            if e1 % 2 == 1:
                o.append( ( e,e1) )
#equiv
o = [ ( e,e1) for e in lst if e%2 == 0
                for e1 in lst if e1 % 2 == 1]
print(o)


#set compre - set - unique - can have filter, multiple for etc
o = set()
for e in lst:
    o.add(e*e)
#equiv
o = { e*e for e in lst  }
print(o)
#dict compre - dict - k:v pairs , can have filters, multiple fors etc
o = {}
for e in lst:
    o[e] = e*e
#equiv
o = { e : e*e for e in lst  }
print(o)