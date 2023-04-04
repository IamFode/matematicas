"""
DEFINICIÓN 1.2

La mediana de un conjunto de observaciones es el valor para el cual, todas las observaciones se ordenan
1.2 de manera creciente, la mitad de éstas es menor que este valor y la otra mitad mayor.
"""

def mediana(lista):
    lista.sort()
    if len(lista)%2==0:
        return (lista[len(lista)//2]+lista[len(lista)//2-1])/2
    else:
        return lista[len(lista)//2]

#ejemplo
print(mediana([2,1,4,3,5,6,2,7,9,3]))
