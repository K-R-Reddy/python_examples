f=open("new.txt",'r')
print(f.read())
f.seek(0)
print(f.read(4))
print(f.tell())
f.seek(5)
print(f.read(2))
with open("new2.txt","r") as f1:
    for i in range(3):
        f1.readline()
    print(f1.readline())
