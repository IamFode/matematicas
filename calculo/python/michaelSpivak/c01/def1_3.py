"""
DEFINICIÓN 1.3

Para los números $a$ que satisfagan:
a>0, se llaman positivos
a<0 se llaman negativos.
"""

def def1_3(a):
    if a>0:
        return "{0}>0, se llaman positivos.".format(a)
    elif a<0:
        return "{0}<0, se llaman positivos.".format(a)
    else:
        return "Cero"

