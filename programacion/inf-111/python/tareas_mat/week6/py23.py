import numpy as np

f = lambda x: abs(1/2 - np.cos(x))

x = float(input("ingrese x: "))

print(f(x))
