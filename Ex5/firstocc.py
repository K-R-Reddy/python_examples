l=[]
n=int(input("Enter no of elements : "))
for i in range(n):
    ele=int(input())
    if ele not in l:
        l.append(ele)
    else:
        pass
print(l)
e=int(input("Enter element to Remove : "))
if e in l:
    l.remove(e)
    print(l)
else:
    print("Element not found")
