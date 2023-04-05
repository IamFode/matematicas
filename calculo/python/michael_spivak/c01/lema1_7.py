"""
Demostrar que (− a)( − b) = a · b
"""

def lema1_7Num(a, b):
    der = (-a)*(-b)
    izq = a*b
    return "{0} = {1}".format(der, izq)
