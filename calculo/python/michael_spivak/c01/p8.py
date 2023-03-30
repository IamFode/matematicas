"""
Si a y b son números cualesquiera, entonces
a*b=b*a
"""

def prop8(a,b):
    return "Si {0} y {1} son números cualesquiera, entonces \n {0}*{1}={0}*{1}".format(a,b)

def prop8Num(a,b):
    multder = a*b #multiplicación de a por b
    multizq = b*a #multiplicación de b por a
    print(multder,"=",multizq)
    return multder

