n=int(input("enter a more than one digit number :"))
t,sum=n,0
while t>0:
	r=t%10
	sum+=r
	t=t//10
print("Sum of the digits of ",n," : ",sum)
