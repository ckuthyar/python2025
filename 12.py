import csv
import os

f1=open("1.csv","r")
list1=csv.reader(f1)
for row in list1:
    print(row)




