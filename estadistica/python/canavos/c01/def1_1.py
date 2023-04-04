"""
La media de las observaciones
x_1,x_2,...,x_n 
es el promedio aritmético de estas y se denota por
mean(x) = \sum_{i=1}^n x_i/n
"""

def media(x):
    n = len(x) # suma de los elementos de la lista
    suma = 0 
    for i in range(len(x)): # iterar sobre los elementos de la lista
        suma += x[i] # suma de cada elemento de la lista
    return suma/n # total de la suma de los elementos sobre el número de elementos

