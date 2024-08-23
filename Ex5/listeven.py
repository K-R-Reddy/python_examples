l=[]
n=int(input("Enter no of elements : "))
for i in range(n):
    ele=int(input())
    l.append(ele)
print(l)
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even : ",even)
print("Odd : ",odd)