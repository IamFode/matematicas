from sympy import *

# definir una función
x = Symbol("x")
f = (x**3 - 8)/(x-2)
# Operar el límite de la función 
print("El límite es: ",limit(f,x,2))
