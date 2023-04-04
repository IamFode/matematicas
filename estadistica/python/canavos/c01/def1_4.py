"""
DEFINICIÓN 1.4

La varianza de las observaciones x1 , x2 , . . . , xn es, en esencia, el promedio 
del cuadrado  de las distancias entre cada observación y la media del conjunto de 
observaciones. La varianza se denota por
s^2 = sum_(i=1)^n (x_i - x)^2 / (n - 1)
"""

def varianza(x):
    n = len(x) #número de elementos
    suma = 0
    for i in range(n):
        suma += (x[i] - sum(x)/n)**2 #sum(x)/n es la media
    n_1 = suma/n-1
    return  n_1 #n-1 es el denominador

