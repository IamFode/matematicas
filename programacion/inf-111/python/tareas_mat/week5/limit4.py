from sympy import *

# definir una función
x = Symbol("x")
f = (1-(x)**(1/2))/(1-x)
# Operar el límite de la función 
print("El límite es: ",limit(f,x,1))
