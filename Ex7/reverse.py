str=input("Enter any String : ")
print(str[::-1])
re_str=""
for i in str:
    re_str=i+re_str
print("Reversing String :",re_str)
for j in range(len(str)-1,-1,-1):
    print(str[j],end="")
print()
for k in range(-1,(len(str)*-1)-1,-1):
    print(str[k],end="")
print()