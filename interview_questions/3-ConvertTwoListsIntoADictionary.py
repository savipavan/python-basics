'''
Write a program to convert two lists into a dictionary

eg. list1 = [pavan,kumar,venkat,varri]
    list2 = [8412,2541,3521,8546]
'''

def list_to_dict():
    keys = [1,2,3,4]
    values = ["one","two","three","four"]

    result = dict(zip(keys,values))
    print(result)

def dict_to_tuple():
    x = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    for i in x.items():
        print(i)

if __name__ == '__main__':
    list_to_dict()
    dict_to_tuple()