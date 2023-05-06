"""
Si a, b y c son números cualesquiera, entonces
a*(b*c)=(a*b)*c
"""

def prop5(a, b, c):
    return "Si {0}, {1} y {2} son números cualesquiera, entonces \n {0}*({1}*{2})=({0}*{1})*{2}".format(a,b,c)

def prop5Num(a,b,c):
    multder = a*(b*c)
    multizq = (a*b)*c
    print("{0}={1}".format(multder, multizq))
    return multder

