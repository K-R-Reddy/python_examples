def gcd(dd,dr):
    if dr==0:
        return dd
    else:
        rem=dd%dr
        return gcd(dr,rem)
a=int(input("Enter Number 1 : "))
b=int(input("Enter Number 2 : "))
print(gcd(a,b))
