from sympy import *

# definir una función
x = Symbol("x")
f = (1-(1-x**2)**(1/2))/x
# Operar el límite de la función 
print("El límite es: ",limit(f,x,0))
