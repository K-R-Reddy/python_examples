def larglist(b):
    temp=0
    for i in range(0,len(b)-1):
        for j in range(i,len(b)):
            if b[i]>b[j]:
                temp=b[i]
                b[i]=b[j]
                b[j]=temp
    return b[0],b[-1],b[-2]
a=input("Enter any Numbers : ").split()
b=[]
for i in a:
    b.append(int(i))
se,le,sle=larglist(b)
print("Smallest Element :",se)
print("Largest Element :",le)
print("Second Largest Element :",sle)
