with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("Raj eswar")
    print(myfile.read())
myfile.close()
