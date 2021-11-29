# composición de funciones
def fhg(x):
    if (2 - x) >= 0:
        f = lambda x: (x+2)/(3-x)
        g = lambda x: x**2/(x**2 + 1)
        h = lambda x: (2-x)**(1/2)
        return f(g(h(x)))
    else:
        print("2-x debe ser mayor o igual a 0")

n = float(input("Ingrese un número: "))
print(fhg(n))
