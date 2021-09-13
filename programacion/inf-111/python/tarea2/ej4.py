# Variables de entrada
x, z = map(float,input("Número de hombres y mujeres: ").split())

# porcentaje de hombres y mujeres
h = x/(x+z)*100
m = z/(x+z)*100

#Imprimir porcentaje de hombres y mujeres
print('El porcentaje de hombres es: {:.2f} y el de mujeres es {:.2f}'.format(h,m))

