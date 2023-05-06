from definicionesC1.funcCreciente import funcCreciente
import numpy as np

# Función creciente
class FuncionCreciente:

    def __init__(self,x,y,f):
        self.x = x
        self.y = y
        self.f = lambda x: eval(f)

"""
Una función f se dice que es creciente en un conjunto S si f(x)<= f(y) para cada par de puntos
x e y de S con x<y.
"""

    def funcCreciente(x,y,f, S = 0.3): # Variables x,y con la función f y el conjunto S.
        if x<=y: #x<y
            for i in np.arange(x,y,S): 
                print(i)
                if not f(i)<=f(i+S): # f(x)<= f(y)
                    return False
                return True
        else:
            return False
