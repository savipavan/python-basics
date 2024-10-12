import json

path = r"C:\Users\varri\IdeaProjects\python-basics\python_basics_22July_2024\python_advanced_01082024\Day2\example.json"

with open(path) as f:
    obj = json.load(f)

# print(obj)
# print(type(obj))
#
# print(obj[0].keys)

# get all emp id
# print([emp['empId'] for emp in obj])

#Handson - get full names of all emp
# print([emp['details'][['firstName']['lastName']] for emp in obj])
print([emp['details']['firstName'] + " " + emp['details']['lastName'] for emp in obj])
# full names = firstName + lastName

# Homework -1. Get all the cities of all emp who are alive

empList = [emp['details'] for emp in obj]

for emp in empList:
    print(emp["firstName"],emp["lastName"] )

#2 . get office  phones of all alive emps
# Creation of json
# o = {'name':'ok', 'age': 20}
# json.dumps(o)

# install all external modules list
# open pandas ref pdf ; pandas cheat sheet
