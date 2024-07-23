# search() method

# checks for existence
import re

line = "At TTT, we tech you how to perform data manipulation, " \
        "file processing and visualization using Python"
found = re.search("at", line)
if found:
    print('String found')

# search with regular expression
import re

print(re.search('^regular', 'regular expression search test'))
print(re.search('search$', 'test regular expression search'))

## substitute() method
import re
Phonenum = "22343-565-576676-66"
num = re.sub('-',"",Phonenum)
print("Phone Num = ", num)

# substitute() method
import re
Phonenum = "22343-565-576676-66"
num=re.sub('-',"*",Phonenum)
print("Phone Num = ", num)
