"""
DEFINICIÓN 2

Una función f es convexa en un intervalo si, dados a, x y b del intervalo con 
a < x < b, se verifica que 
(f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)
"""
import numpy as np

def convexa(func,i,j):
    f = lambda x: eval(func)
    line = np.linspace(i,j,20)
    for a in line:
        for b in line:
            if a<b: # a < x < b
                for x in line:
                    if (a<x<b): # a < x < b
                        if ((f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)): # (f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)
                            izq = ((f(x)-f(a))/(x-a))
                            der = ((f(b)-f(a))/(b-a))
                            return "{}<{}".format(izq,der)
                        else:
                            izq = ((f(x)-f(a))/(x-a))
                            der = ((f(b)-f(a))/(b-a))
                            return "{}>{}".format(izq,der)
                            break

def convexaBool(func,i,j):
    f = lambda x: eval(func)
    line = np.linspace(i,j,20)
    for a in line:
        for b in line:
            if a<b: # a < x < b
                for x in line:
                    if (a<x<b): # a < x < b
                        if ((f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)): # (f(x)-f(a))/(x-a) < (f(b)-f(a))/(b-a)
                            print("Es convexa")
                            return True
                        else:
                            print("No convexa o concava")
                            return False
                            break



