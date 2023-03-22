import numpy as np

"""
1.20
Una función se dice decreciente en S si f(x)>=f(y) para todo x<y en S. Si f(x)>f(y) para todo x<y en S
la función se denomina decreciente en sentido estricto en S.
"""


def funcDecrecientef(x,y,func,S=0.5): # Variables x,y con la función f y el conjunto S.
    f = lambda x: eval(func)
    if x<=y: #x<y
        for i in np.arange(x,y,S): 
            if not f(i)>=f(i+S): # f(x)>=f(y)
                return False
        return True


def funcDecreciente(x,y,f,S=0.5): # Variables x,y con la función f y el conjunto S.
    if x<=y: #x<y
        for i in np.arange(x,y,S): 
            if not f(i)>=f(i+S): # f(x)>=f(y)
                return False
        return True

