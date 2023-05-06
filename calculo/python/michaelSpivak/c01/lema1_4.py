"""
LEMA 1.4

Si a-b=b-a entonces a=b.
"""

def lema1_4(a, b):
    if a-b == b-a: # Si a-b=b-a
        return "Si {0}-{1}={1}-{0} entonces {0}={1}".format(a, b)
    else:
        return "a-b no es igual a b-a"

def lema1_4Num(a,b):
    if a-b == b-a: # Si a-b=b-a
        return True
    else:
        return False
