from sympy import *

# definir una función
x = Symbol("x")
f = (x**2-1)/(x+1)
# Operar el límite de la función 
print("El límite es: ",limit(f,x,1))
