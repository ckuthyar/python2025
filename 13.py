import csv
import os

f1=open("1.csv","r")
f2=open("2.csv","w")
list1=csv.reader(f1)
for row in list1:
    print(row)
    f2.write(str(row))
    f2.write("\n")
f2.close()



