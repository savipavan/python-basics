try:
    x=int(input('Enter number: '))
    y=int(input('Enter number: '))
    print(x/y)
except ZeroDivisionError:
    print('Cannot divide  number by zero')
except ValueError:
    print('OOPS! That was not a valid number. Try Again')