def Arith(a,b):
    return a+b,a-b,a*b,a/b
def Arith1(a,b):
    return [a+b,a-b,a*b,a/b]
x=int(input("Enter value 1 : "))
y=int(input("Enter value 2 : "))
print(Arith(x,y))
print(Arith1(x,y))
print([Arith(x,y)])
add,sub,mul,div=Arith(x,y)
print(add,sub,mul,div)