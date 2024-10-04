i="""\nThis is multi
Lined input
into the File"""
f=open("new2.txt",'w')
f.write("This is write mode")
f.writelines(i)
print("File Writed")