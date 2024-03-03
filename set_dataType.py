#Set Data Type  
a = {1,2,3,4,5}
b = {4,5,6,7}
c = a.intersection(b)
print(type(a))
print(c.add(7))
print(a.union(b))

# Frozen Set        #Frozen set cannot modify
f = frozenset({1,2,3,4,5})