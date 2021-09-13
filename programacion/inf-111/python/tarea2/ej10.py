# variables de entrada
total = float(input("Total Venta: "))
pago = float(input("Pago: "))

c = round(pago - total,2)
cambio = round(c,2)

# procedimiento
cinco = int(cambio/5)
cambio = 5*(cambio/5 - cinco)
dos = int(cambio/2)
cambio = 2*(cambio/2 - dos) 
uno = int(cambio)
cambio = (cambio - uno)
cincuenta = int(cambio/0.5)
cambio = 0.5*(cambio/0.5 - cincuenta)
veinte = int(cambio/0.2)
cambio = 0.2*(cambio/0.2 - veinte)
diez = int(cambio/0.1)

#imprimir
print("CAMBIO: ", c)
print("5 bolivianos: ", cinco)
print("2 bolivianos: ", dos)
print("1 boliviano: ", uno)
print("50 centavos: ", cincuenta)
print("20 centavos: ", veinte)
print("10 centavos: ", diez)
