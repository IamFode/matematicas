"""
LEMA 1.6

Demostrar que (-a)b=-(ab)
"""

def lema1_6Num(a,b):
    izq = (-a)*b
    der = -(a*b)
    return "{0} = {1}".format(izq,der)

