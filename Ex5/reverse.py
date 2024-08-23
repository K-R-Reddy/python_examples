l=[]
n=int(input("Enter no of elements : "))
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
l.reverse()
print(l)
print(l[::-1])
