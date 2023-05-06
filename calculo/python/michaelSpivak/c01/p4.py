"""
Si a y b son números cualesquiera, entonces
a + b = b + a
"""

def prop4(a, b):
    return "Si {0} y {1} son números cualesquiera, entonces \n {0}+{1}={1}+{0}".format(a, b)

def prop4Num(a, b):
    sumader = a+b
    sumaizq = b+a
    print("{0}={1}".format(sumader, sumaizq))
    return sumader

