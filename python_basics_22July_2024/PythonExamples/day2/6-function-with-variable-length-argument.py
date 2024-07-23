# Variable length arguments
def printdata(*names):
    print('type of passed argument is ', type(names))
    print('printing the passed arguments...')
    for name in names:
        print(name)

printdata('pavan','kumar','varri','venkata')
printdata('pavan', 45, 0.1, 'kumar')