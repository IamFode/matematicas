import numpy as np

f = lambda x, n : (np.sin(n*x)/2*np.cos((n+1)*x/2)) / (np.sin(x/2))

x = float(input("ingrese x: "))
n = float(input("ingrese n: "))

print(f(x,n))
