import numpy as np

f = lambda x: abs(np.sin(x) - np.cos(x))

x = float(input("ingrese x: "))

print(f(x))
