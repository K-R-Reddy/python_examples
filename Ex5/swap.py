l=[]
n=int(input("Enter no of elements : "))
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
n1=int(input("Enter 1st element place to swap : "))
n2=int(input("Enter 2nd element place to swap : "))
l[n1-1]=l[n2-1]+l[n1-1]
l[n2-1]=l[n1-1]-l[n2-1]
l[n1-1]=l[n1-1]-l[n2-1]
print(l)