import csv
import os
data={"name":"Kuthyar", "city":"Bangalore"}
f1=open("1.csv","r")
f2=open("2.csv","w")

with open("1.csv",mode="r") as f1:
    reader=csv.reader(f1)
    for row in reader:
        print(row)

with open("output1.csv",mode="w") as f2:
    writer=csv.writer(f2)
    for row in data:
        writer.writerow(data)
    




