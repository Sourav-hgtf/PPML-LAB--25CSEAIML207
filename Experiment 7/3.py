from math import pow

x = list(eval(input("Enter the power list: ")))
y = list(eval(input("Enter the number list: ")))

def power(x, y):
    z = int(pow(y, x))
    return z

l = list(map(power, x, y))

print("The resultant list:", l)