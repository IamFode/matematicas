import numpy as np
from scipy.integrate import quad

def integ(x,a,b):
    integral1 =  1/b * (np.sin(a+b*x)+np.sin(a))
    integral2 = -1/b * (np.cos(a+b*x)-np.cos(a))
    return "{}, {}".format(integral1,integral2)

x = float(input("introducir x: "))
a = float(input("introducir a: "))
b = float(input("introducir b: "))

print(integ(x,a,b))
