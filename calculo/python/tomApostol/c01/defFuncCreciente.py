import numpy as np
"""
Una función f se dice que es creciente en un conjunto S si f(x)<= f(y) para cada par de puntos
x e y de S con x<y.
"""

def funcCrecientef(x,y,func,S=0.5): # Variables x,y con la función f y el conjunto S.
    f = lambda x: eval(func)
    if x<=y: #x<y
        for i in np.arange(x,y,S): 
            if not f(i)<=f(i+S): # f(x)<= f(y)
                return False
        return True


def funcCreciente(x,y,f,S=0.5): # Variables x,y con la función f y el conjunto S.
    if x<=y: #x<y
        for i in np.arange(x,y+0.01,S): 
            if not f(i)<=f(i+S): # f(x)<= f(y)
                return False
        return True

