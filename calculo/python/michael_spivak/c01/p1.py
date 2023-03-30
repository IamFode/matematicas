"""
(P1)
Si a,b y c son números cualesquiera, entonces
a+(b+c) = (a+b)+c
"""

def prop1(a,b,c):
    return "{0}+({1}+{2})=({0}+{1})+{2}".format(a,b,c)

def prop1Num(a,b,c):
    sumader = a+b+c
    sumaizq = a+(b+c)
    print("{0} = {1}".format(sumader,sumaizq))
    return sumader

