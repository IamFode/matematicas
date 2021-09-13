# Librería math
import math

# Variables de entrada

r, a = input("Ingrese el radio y la altura de un cono: ").split()

#formula de volumen

vol = (1/3) * math.pi * r**2 * a 

#imprimir
print("El volumen es ", vol)
