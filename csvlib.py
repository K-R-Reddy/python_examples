import csv
data=[['SNO','ROLL NUMBER','NAME','PHONE'],
      [1,512,'Rajeswar',9491332342],
      [2,513,'Jagadeesh',9349922398],
      [3,514,'Hari Krishna',8654678989]]
with open("new4.csv","w",newline="") as f:
    fwrite=csv.writer(f)
    fwrite.writerows(data)
f1=open("new4.csv","r")
fread=csv.reader(f1)
for row in fread:
    print(row)