# The function simple_interest accepts three arguments and retuns the simple interest accordingly

def simple_interest(p,r,t):
    return (p*t*r) / 100

p = float(input("Enter the principle: "))
r = float(input("Enter the interest: "))
t = float(input("Enter the years: "))

print("Simple Interest: {}".format(simple_interest(p,r,t)))
print("simple interest1: ", simple_interest(p,r,t))