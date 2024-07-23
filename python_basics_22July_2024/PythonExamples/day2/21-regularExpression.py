#findall() method
import re
str="How are you. how is everything"
matches = re.findall("How",str,re.I) #re.I means ignore case
print(matches)
print(type(matches))

#method() method
import re
pincode = input("Enter pincode : ")
pattern = r'\d\d\d \d\d\d'
matchobj = re.match(pattern,pincode)
print(matchobj)
print(type(matchobj))