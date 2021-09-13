# variables de entrada
x1, y1, x2, y2 = map(float,input("Ingrese x1, y1, x2 , y2: ").split())

# Distancia de dos puntos
d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

#Imprimir distancia
print("{:.2f}".format(d))
