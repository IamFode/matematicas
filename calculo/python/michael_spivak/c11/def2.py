"""
DEFINICIÓN 2

Una función f es convexa en un intervalo si, dados a, x y b del intervalo con 
a < x < b, se verifica que 
(f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)
"""
import numpy as np

def convexaBool(i,j,func,n):
    f = lambda x: eval(func)
    line = np.linspace(i,j,n)
    for a in line:
        for b in line:
            # a < x < b
            if a<b:
                for x in line:
                    # a < x < b
                    if (a<x<b):
                        # (f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)
                        if ((f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)):
                            return True
                        else:
                            return False
                            break

print(convexaBool(-1,0,'x**3+x',10))

