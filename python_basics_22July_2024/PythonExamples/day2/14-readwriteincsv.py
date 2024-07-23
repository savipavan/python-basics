# data in csv file

# writerow() method
import csv
products = [(1, 'mobile',2500,10),(2,'laptop',50000,5),(3,'pen',25,100)]
csvfile = open("data.csv","w",newline='')
obj = csv.writer(csvfile) #obj is a writer class
for p in products:
    obj.writerow(p) #writerow is a method
csvfile.close()

#Writerows() method
import csv
products1 = [(1, 'mobile',2500,10),(2,'laptop',50000,5),(3,'pen',25,100)]
csvfile1 = open("data1.csv","w",newline='')
obj = csv.writer(csvfile1)
obj.writerows(products1) #Write Collection
csvfile.close()

# Read dictionary values from file
import csv
csvfile = open("data.csv","r",newline='')
obj = csv.reader(csvfile) #reader object
for row in obj:
    print(row)
csvfile.close()