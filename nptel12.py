str1=input("Enter first String : ")
str2=input("Enter second String : ")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")
