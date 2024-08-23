n=int(input("Enter no of rows : "))
t=65
for i in range(1,n+1):
	for j in range(1,i+1):
		print(chr(t),end=" ")
		t+=1
	print() 
