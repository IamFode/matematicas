"""
Para todo número a, existe un número -a tal que
a+(-)=(-a)+a=0
"""

def prop3(a):
    return "{0}+(-{0})=(-{0})+{0}=0".format(a)

def prop3Num(a):
    sumader = a-a
    sumaizq = -a+a
    print("{0}={1}=0".format(sumader,sumaizq))
    return sumader
