# Variable de entrada
año = int(input("Ingrese la cantidad de años: "))

# conversión de año a seg
conv = 365*24*60*60

# total de personas que nacen mueren y emigran
pob = conv*(1/7 - 1/13 + 1/45)

# Población estimada y redondeada al entero superior
pob_total = round(312032486 + (año*pob))

# Imprimir
print("La población después de {} será de {}".format(año,pob_total))
