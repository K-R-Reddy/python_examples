def gcd(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1
a=int(input("Enter Number 1 : "))
b=int(input("Enter Number 2 : "))
print("GCD of",a,",",b,":",gcd(a,b))
