a=int(input("enter a value :"))
b=int(input("enter b value :"))
c=int(input("enter c value :"))
if(a>=b and a>=c):
    print(a," is largest")
elif(b>=c):
    print(b," is largest")
else:
    print(c," is largest")