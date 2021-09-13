# variable de entrada
p = float(input("Ingrese el total: "))

# descuento
d = p*0.1

# Total a pagar
tp = p-d

#imprimir descuento y total a pagar
print("El descuento es de: {:.2f} \nEl total a pagar es: {:.2f}".format(d,tp))
