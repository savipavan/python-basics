'''
Dictionary is a mutable collection
in dictonary items will be in the key:value pair

dictionary = {key1: value1, key2: value2, key3: value3}

empty_list = []
empty_tuple = ()
empty_dict = {}

'''

# Create dictionary using {}
# alternative is dict()
my_empty_dict = {} # alternative: my_empty_dict = dict()
print('empty dict: {}, type: {}'.format(my_empty_dict, type(my_empty_dict)))

# Dictonary initilizations
userDetails = {'name': 'pavan', 'age': 25, 'city': 'chennai'}
print(userDetails)

# add new entries
userDetails['state'] = 'tamilnadu'
print(userDetails)

# empty dictionary declation
userDetails = {}

#populate dictionary entries
# for i in range(3):
#     key = input("Enter parameter:")
#     value = input("Enter value: ")
#     userDetails[key] = value

print(userDetails)

# user details used in the example below:
userDetails = {"name": "pavan", "age": 25, "city": "chennai"}
print(userDetails)

# retrieve
print("user name: ", userDetails["name"])

# entry will be updated or added based on whether key exists or not update
userDetails["city"] = "hyderabad"
print(userDetails)

# add new entry(key-value pair)
userDetails["phone"] = "123456"
print()

# get all keys, values methods
print(type(userDetails.values()))

for k in userDetails.keys():
    print(k, ":", userDetails[k])

# get all values
print(userDetails.values())

# Check for existence
print("loc as key exists: ", "loc" in userDetails)
print("city as key exists: ", "city" in userDetails)

# iterate through all key-value pairs
for key, value in userDetails.items():
    print("{}:{}".format(key, value))

# returns the value. if not found, returns message
print(userDetails.get("city", "Not found"))

# remove key-value pair
del userDetails["phone"]
print("phone entry deleted")
print(userDetails)

# returns keys by default
print("Contents of userDetails")
for user in userDetails:
    print("{} - {}".format(user, userDetails[user]))

# clears the dict
userDetails.clear()
print("Contents of userDetails after clear")
for user in userDetails:
    print(user)