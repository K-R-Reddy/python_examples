def rev(a):
    b=[]
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    return b
l=input("Enter any List : ").split()
print("Given List :",l)
print("Reversed List :",rev(l))