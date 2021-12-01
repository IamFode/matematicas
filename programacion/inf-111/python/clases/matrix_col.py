import numpy as np

array = np.empty((3,3),int)
print(array)

# imprimir por columnas
def imprimirPorColumnas(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[j][i] = 0
    return matriz

print(imprimirPorColumnas(array))
