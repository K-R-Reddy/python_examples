# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
d=int(input())
q=int(input())
if t in ["V","N"] and d>0 and q>0:
    if t=='V':
        if d>0 and d<4:
            print(120*q)
        elif d>4 and d<7:
            print(120*q+((d-3)*3))
        else:
            print(120*q+(((d-6)*6)+9))
    else:
        if d>0 and d<4:
            print(150*q)
        elif d>4 and d<7:
            print(150*q+((d-3)*3))
        else:
            print(150*q+(((d-6)*6)+9))
else:
    print("-1")