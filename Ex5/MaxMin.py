l=[]
n=int(input("Enter no of elements : "))
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
print("Maximum Number Place : ",(l.index(max(l))+1))
print("Mininum Number Place : ",(l.index(min(l))+1))