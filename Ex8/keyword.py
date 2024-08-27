def keyword(a=0,b=0,c=1):
    print(a,b,c)
    print(a+b/c)
def key2(a=12,*num):
    print(a)
    print(*num)
    sum=0
    for i in num:
        sum=sum+i
    print(sum)
def key3(*num,a=42):
    print(a)
    print(*num)
keyword(12,13)#default
keyword(15,c=18)#positional-default-keyword
keyword(10)#default
keyword()#default
keyword(1,1,1)#postional
keyword(b=41,c=57,a=26)#keyword
keyword(2,c=94,b=52)#positional-keyword
key2(1,2,3,4,5,6,7,8,9,10)#variable-length
key2(42)
key2()
#key2(1,2,3,4,a=9)
key3(12,34,56,78)