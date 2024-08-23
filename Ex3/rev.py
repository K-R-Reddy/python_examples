n=int(input("enter a more than one digit number :"))
t,rev=n,0
while t>0:
	r=t%10
	rev=(rev*10)+r
	t=t//10
print("Reverse of the number ",n," : ",rev)
