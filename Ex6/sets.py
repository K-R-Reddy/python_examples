a={1,2,3,4,1,4,'hello'}
b=set((5,9,2))
print(a)
print(a|b)#UNION
print(a&b)#INTERSECTION
print(a-b)#DIFFERENCE
print(a^b)#SYMMETRIC DIFFERENCE
print('''hello''' in a)
print('hello' not in a)
a.add(5)
a.discard(2)
a.pop()
a.remove(4)
print(a)
c=b.copy()
b.clear()
print(b)
print(c)
print(a.difference(c))
c.symmetric_difference_update(a)
print(c)
print(a.issubset(c))
print(a.issuperset(c))
print(b.issubset(a))
print(c.union(a))
print(a.intersection(c))
