def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(first_pos<last_pos and flag==0):
        count+=1
        mid=int((first_pos+last_pos)/2)
        if(x==a[mid]):
            flag=1
            print(x,"is found at position ",mid+1)
            print("Iterations :",count)
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
    if(flag==0):
        print(x,"is not found")
            
a=[]
for i in range(1,501):
    a.append(i)
x=int(input("Enter element to search : "))
binary_search(a,x)