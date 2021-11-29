
# Composición de funciones para f g y h
def fgh(x):
    if x == 0 or x == -1/4:
        print("x debe ser diferente a 0 o -1/4")
    else:
        f = lambda x: (x+1)**(1/2)
        g = lambda x: 1/(x+4)
        h = lambda x: 1/x
        return f(g(h(x)))

n = float(input("Ingrese un número: "))
print(fgh(n))
