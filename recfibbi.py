def fibbi(n):
    if n<=1:
        return n
    else:
        return (fibbi(n-1)+fibbi(n-2))
a=int(input("Enter any Number : "))
for i in range(a):
    print(fibbi(i))
