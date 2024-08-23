n=int(input("Enter any number :"))
factors=0
for i in range(2,n):
	if(n%i==0):
		factors+=1
if(factors==0):
	print(n,"is Prime number")
else:
	print(n,"is not a Prime number")

