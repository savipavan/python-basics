# Raising an exception
def acceptNumber():
    x=int(input('Enter number: '))
    if x<=0:
        raise Exception('Value should be greater then 0')
try:
    acceptNumber()
except Exception as ex:
    print(ex)