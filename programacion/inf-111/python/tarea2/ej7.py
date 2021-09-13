# Variables de entrada
mt, p = map(float,input("Ingrese el monto total y el porcentaje de la propina: ").split())

# monto de propina
mp = mt*(p/100)

#Total a pagar
tp = mt + mp

#imprimir
print("La propina es de Bs {:.2f} y el total a pagar es Bs {:.2f}".format(mp,tp))
