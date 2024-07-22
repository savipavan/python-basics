# String indexing : grab a single character at the given index
# Strings are sequence of character, each character has an index starting with 0

name = "pavan kumar"
print(name[3])

# String slicing : grab a substring from a given string, for that we need to pass starting index and stoping index.. we also pass step or jum index

# [start index: stop index : step index]
# Start index = it starts grabing character from start index
# stoping index: it goes till stop index, but take one character less than stop index
# step : jump

print(name[0:8])

my_string = "JPMorgan"

# string indexing
print(my_string[0])
print(my_string[3])
print(my_string[-1])

# string slicing
print(my_string[2:])
print(my_string[:4])

# step
print(my_string[2:6])
print(my_string[2:6:2])

print(my_string[::2])
print(my_string[2:7:2])

print(my_string[::-1])

## Strings are immutable
name = "pavan"

# String Immutability
str = 'hello'
# print(str)
# str[0] = 'H'

newstr = str[1:]
print(newstr)
str = 'H'+newstr
print(str)

# String join str.join
pandas = 'pandas'
numpy = 'numpy'
requests = 'requests'
cool_python_libs = ','.join([pandas, numpy, requests])
print('Some cool python libraries: {}'.format(cool_python_libs))

# str.upper(), str.lower(), str.title()
mixed_case = 'PyTHon hackER'
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.title())

# str.strip(), str.lstrip(), str.rstrip()
str = ' \n \t Some story to tell  '
stripped = str.strip()

print('ugly: {}'.format(str))
print('stripped: {}'.format(str.strip()))

print(str.strip())
print(str.lstrip())
print(str.rstrip())

string = '@@@@@@Geeks for Geeks @@@@'
# String all '@' from beginning and ending
print(string.strip('@'))

# str.split()
sentence = 'three different words'
words = sentence.split()
print(words)
print(type(words))

# str.split by comma
secret_binary_data = '01001,101101,11100000'
binaries = secret_binary_data.split(',')
print(binaries)
print(type(binaries))

# str.replace()
doyouknow = "Python is my favorite language"
my_modified_string = doyouknow.replace('is', 'willbe')
print(my_modified_string)

pavan = "varri"
kumar = pavan.replace('h', 'p')
print(kumar)

# Calling multiple method in a row
ugly_mixed_case = '      ThIS LooKs BAd '
pretty = ugly_mixed_case.strip().lower().replace('bad', 'good')
print(pretty)

# escape character - indented
indented = '\tThis will be indented'
print(indented)

