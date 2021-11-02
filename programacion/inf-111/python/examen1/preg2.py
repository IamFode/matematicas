

m = int(input("Cantidad de mujeres: "))
h = int(input("Cantidad de hombres: "))

porcentaje_h = (h * 100) / (m + h)
porcentaje_m = (m * 100) / (m + h)

print("El porcentaje de mujeres es: {:.2f}, y el porcentaje de hombres es {:.2f}".format(porcentaje_m,porcentaje_h))
