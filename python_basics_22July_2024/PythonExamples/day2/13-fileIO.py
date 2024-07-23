filename = input("enter filename : ")
fileptr = open(filename, 'w')
print("Name of the file: ", fileptr.name)
print('Closed or not: ', fileptr.closed)
print('Opening mode : ', fileptr.mode)

# Open file handle for writing
f = open("raw_strings.txt", 'w')
f.write("First line here \n")
f.write("Second line here \n")
str_list = ["some more lines ....\n", "This is a new line \n", "created from list of strings\n"]
f.writelines(str_list)
f.close()

# open file for reading
f = open('raw_strings.txt')
# read all the contents of the file into a variable
data = f.read()
for ch in data:
    print(ch, end="")
# Contents of the variable
print(data)

# does the readline function return any value
# if not, why?
position = f.tell()
f.seek(5)
data_line = f.readline() # Guess the output
print(position)
print(data_line, end="")