#imprimir por filas
import numpy as np

array = np.empty((3,3),int)
print(array)

def llenarConCeros(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = 0
    return matriz

print(llenarConCeros(array))
