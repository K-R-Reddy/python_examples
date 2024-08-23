s1='Single'
s2="DOUBLE"
s3='''Hello!
   Python'''
print(s1)
print(s2)
print(s3)
print(s3[0:22:3])
print("s1+s2 :",s1+s2)
print("s1 * 3 :",s1*3)
print("s2[0] :",s2[0])
for i in s3:
    print(i)
print('e' in s1)
print('e' not in s2)
print("String Methods : ")
print(s1.upper())
s4='HELLOOOOOOOOOOOOOO wOrld!'
print(s4.lower())
print(s4.capitalize())
print(s1.center(30,'-'))
print(s4.count('O'))
print(s2.isupper())
print(s1.islower())
w='abc@123'
x='cvr123'
y='cvr'
z='123'
print(y.isalpha())
print(w.isalnum())
print(x.isalnum())
print(z.isdigit())
print(s4.replace('wOrld','WORLD'))
print(s4.title())
i="My name is {1} and my age is {0}".format(s1,s2)
print(i)
