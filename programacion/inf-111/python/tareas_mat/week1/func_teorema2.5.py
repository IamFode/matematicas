import numpy as np

def teorema5_1(a,b):
    coseno = np.sin(b) - np.sin(a)
    seno = -(np.cos(b)-np.cos(a))
    print("La integral del coseno viene dado por: {}\nLa integral del seno viene dado por: {}".format(coseno,seno))

a = float(input("Ingresar el primer número (a) del rango de la integral : "))
b = float(input("Ingresar el segundo número (b) del rango de la integral : "))

teorema5_1(a,b)



