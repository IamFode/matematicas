"""
b1 = (\sum (y_i-media(y))(x_i-media(x))) / (sum(x_i-media(x)))**2)
"""

media = lambda x: sum(x)/len(x)

def b1(x, y):
    """ Calcula el coeficiente de correlación entre dos variables

    Args:
        x: lista de valores de la variable independiente
        y: lista de valores de la variable dependiente

    Returns:
        Float con el valor del coeficiente de correlación
    """

    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud")

    numerador = sum([(x[i] - media(x)) * (y[i] - media(y)) for i in range(len(x))])
    denominador = sum([(x[i] - media(x))**2 for i in range(len(x))])

    return numerador / denominador

def b0(x, y):
    return media(y) - b1(x, y) * media(x)

def varError(x,y):
    """ Calcula la varianza del error """

    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud")

    var = (1/(len(x)-2))*sum([(y[i] - b0(x, y) - b1(x, y) * x[i])**2 for i in range(len(x))])
    return var


import numpy as np

x = np.array([1, 2, 4, 4, 3])
y = np.array([1, 3, 1, 3, 5])

print(varError(x, y))

# Usando sklearn
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x.reshape(-1, 1), y)
y_pred = reg.predict(x.reshape(-1, 1))
residuos = y - y_pred
varianza = np.var(residuos, ddof=2)
print(varianza)
