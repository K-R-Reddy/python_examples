n=input().split(' ')
print(*n,sep='----',end='\t')
l='#'.join(n)
print(l)
m=l.split('#')
print(*m)
o='     this is use of strip method      '
print(o,end='.')
print('\n',o.strip(),end='.')
l=[1,2,3,4]
r=[5,6,7,8]
p=[]
p=[x+y for x,y in zip(l,l)]
print('\n',p)
def pow(y):
    return y**2
result=map(pow,l)
print(list(result))
result2=map(lambda x,y: x*y ,l,r)
print(list(result2))
