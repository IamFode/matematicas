
"""
COMBINACIÓN LINEAL
Una combinación lineal de una lista v_1, v_2, ..., v_n de vectores en V es un vector de la forma
a_1v_1 + a_2v_2 + ... + a_nv_n,
donde a_1, a_2, ..., a_n existen en F.
"""


def combinacionLineal(n):
    suma = []
    for i in range(n):
        a = float(input("Introduce el escalar a{}: ".format(i+1)))
        entrada = input("Introduce el vector v{} separados por espacios: ".format(i+1))
        v = [float(x)*a for x in entrada.split()]
        if i == 0:
            suma = v
        else:
            suma = [x + y for x, y in zip(suma, v)]
    return suma


print(combinacionLineal(2))

