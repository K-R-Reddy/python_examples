n=int(input("Enter no of rows :"))
for i in range(n):
	for j in range(n-i-1):
		print(" ",end="")
	c=1
	for k in range(i+1):
		print(c,end=" ")
		c=c*(i-k)//(k+1)
	print()
