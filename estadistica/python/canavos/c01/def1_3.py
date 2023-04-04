"""
La moda de un conjunto de observaciones es el valor de la observación que ocurre con mayor 
frecuencia en el conjunto.
"""

def moda(lista):
    frecuencias = []
    for i in lista:
        frecuencias.append(lista.count(i))
    return lista[frecuencias.index(max(frecuencias))]

#ejemplo
print(moda([1,2,3,2,4,5,2,7,8,2,1]))
