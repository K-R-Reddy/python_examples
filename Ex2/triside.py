a=int(input("enter a side : "))
b=int(input("enter b side : "))
c=int(input("enter c side : "))
if(a+b>c and a+c>b and b+c>a):
    print("Triangle is valid")
else:
    print("Triangle is Invalid")