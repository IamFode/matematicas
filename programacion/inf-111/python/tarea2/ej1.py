# Importar librería math
import math

# Valores de entrada
r, h = map(float,input("Ingrese el radio y la altura de un cilindro: ").split())

# Fórmula de volumen
v = math.pi * r**2 * h

#Imprimir volumen
print("El volumen es: {:.1f}".format(v))
