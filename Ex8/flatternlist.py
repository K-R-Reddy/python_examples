def flatten(lst):
    return [item for sublist in lst for item in sublist]
a=int(input("Enter How many sub strings in list : "))
c=[]
for i in range(0,a):
    b=input("Enter Values into sub string : ").split()
    c.append(b)
print("Actual List is",c)
print("Flatten List is",flatten(c))
