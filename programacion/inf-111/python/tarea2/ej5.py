# variables de entrada
d=float(input('Introduzca la distancia a recorrer (km): '))
kl=float(input('Ingrese los Kilómetros por un litro: '))
p=float(input('Ingrese el precio por litro: '))

#formula
c = (d/kl)*p 

# Imprimir
print("El costo de conducción es de Bs {:.2f}".format(c))
