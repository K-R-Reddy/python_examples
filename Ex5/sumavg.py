l=[]
n=int(input("Enter no of elements : "))
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
print("Sum of Elements : ",sum(l))
print("Avg of Elements : ",(sum(l)/len(l)))