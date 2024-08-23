n=int(input("enter a more than one digit number :"))
t,rev=n,0
while t>0:
	r=t%10
	rev=(rev*10)+r
	t=t//10
if(rev==n):
	print(n," is a Palindrome")
else:
	print(n," is not a Palindrome")
