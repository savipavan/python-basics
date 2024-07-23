import csv
employees = [{'name':'john','dept':'hr','salary':50000},
             {'name':'Mary','dept':'sales','salary':60000},
             {'name':'Peter','dept':'sales','salary':70000},]

fields = list(employees[0].keys())
csvfile = open('empdata.csv','w',newline='')
obj = csv.DictWriter(csvfile, fieldnames=fields) # writer object
obj.writeheader() #write header
obj.writerows(employees) #Write value / row
csvfile.close()

# read the csv data
csvfile = open('empdata.csv','r',newline='')
obj = csv.DictReader(csvfile, fieldnames=fields) # read object
for field in obj.fieldnames:
    print(field, end="\t")
print()
for row in obj:
    print(row.values())
csvfile.close()