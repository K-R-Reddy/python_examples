n=int(input("enter a number :"))
d=str(n)
t,sum=n,0
while t>0:
	r=t%10
	sum+=(r**len(d))
	t=t//10
if(sum==n):
	print(n,"is a Armstrong number")
else:
	print(n,"is not a Armstrong number")
