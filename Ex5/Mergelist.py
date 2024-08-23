l1=['M','NA','I','RED']
l2=['Y','ME','S','DY']
l3=[]
for x in range(4):
    l3.append(l1[x]+l2[x])
print(l3)
l4=[x+y for x,y in zip(l1,l2)]
print(l4)