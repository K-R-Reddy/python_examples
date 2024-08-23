per=float(input("Enter your percentage : "))
if(per<=100 and per>=90):
    print("Grade A")
elif(per<90 and per>=80):
    print("Grade B")
elif(per<80 and per>=70):
    print("Grade C")
elif(per<70 and per>=60):
    print("Grade D")
elif(per<60 and per>=50):
    print("Grade E")
elif(per>0 and per<50):
    print("Failed")
else:
    print("Invalid Percentage")