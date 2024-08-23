str=input("ENTER ANY STRING : ")
c,v=0,0
for i in str:
    if i in "aeiouAEIOU":
        v+=1
    elif i in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
        c+=1
    else:
        continue
'''METHOD2
for i in str:
    if i.isalpha():
        if i in "aeiouAEIOU":
            v+=1
        else:
            c+=1'''
print("VOWELS COUNT :",v)
print("CONSONANTS COUNT :",c)
print("OTHER CHARACTERS COUNT :",len(str)-v-c)  #OTHER CHARACTERS
