filenames = ["1.Raw data.txt","2.Reports.txt","3.Presentations.txt"]
print(filenames)

for file in filenames:
    file = file.replace('.','-', 1)
    print(file)