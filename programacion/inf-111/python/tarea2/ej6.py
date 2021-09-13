# variable de entrada
min = int(input("Ingrese la cantidad de minutos: "))

# conversión a años
conv = min*(1/60)*(1/24)*(1/365)

#parte entera y parte decimal
año = int(conv)
p_d = abs(conv) - abs(int(conv))

# conversión a días
dia = int(p_d*(365))

# imprimir
print("{} minutos es aproximadamente {} años y {} días".format(min,año,dia))

