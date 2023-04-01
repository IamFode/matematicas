"""
DEFINICIÓN 1.2

El simbolo a/b significa ab^(-1). Puesto que 0^(-1) no tiene sentido, tampoco lo tiene a/0.
La división por 0 es siempre indefinida.
"""

def def1_2(a,b): 
    if b != 0: 
        return "El símbolo {0}/{1} significa {0}*{1}**(-1)".format(a,b)
    else:
        return "b=0 no tiene sentido, por lo tanto a/0 es indefinido"


def def1_2Num(a,b):
    if b != 0: # condición para que la división sea definida
        return a*b**(-1) # a/b
    else:
        return "Indefinido" 
