"""
Si a es cualquier número, entonces
a+0=0+a=a
"""

def prop2(a):
    return "{0}+0=0+{0}={0}".format(a)

def prop2Num(a):
    sumader = a + 0
    sumaizq = 0 + a
    print("{0}={1}={2}".format(sumader, sumaizq,a))
    return sumader
