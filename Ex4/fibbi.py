n=int(input("enter any number : "))
n1,n2=0,1
print(n1)
print(n2)
for i in range(n-2):
	n3=n1+n2
	n1=n2
	n2=n3
	print(n3)
