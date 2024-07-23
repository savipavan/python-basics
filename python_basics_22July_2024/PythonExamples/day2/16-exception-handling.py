i, j = 10,0
div = 0

def exceptTest(p,q):
    try:
        div = p / q
        print("Result: ".format(div))
    except ZeroDivisionError as ze:
        print("Error is: ",str(ze))
    except:
        print("Generic exception")
    finally:
        q = 1
    return p,q

i, j = exceptTest(i, j)
print("i = {}, j={}".format(i,j))