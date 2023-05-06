"""
TEOREMA 1

Sea f convexa. Si f es diferenciable en a, entonces la gráfica de f se sitúa
por encima de la tangente a f en el punto (a, f(a)) y excepto en el mismo punto de
contacto (a, f(a)). Si a < b y f es diferenciable en a y en b, entonces f'(a) < f'{b).
"""

import sys
sys.path.append("..")
from def2 import convexaBool
from c09.defDiferenciable import diferenciableBool
from c09.defDiferenciable import diferenciable

def teo1(f,a,b,h):
    if convexaBool(f,a,b)==True: # Si f es convexa
        if diferenciableBool(f,a,h)==True: # Si f es diferenciable en a
            if diferenciableBool(f,b,h)==True: # Si f es diferenciable en b
                if a<b: # Si a<b
                    return "{}<{}".format(diferenciable(f,a,h),diferenciable(f,b,h))
                else:
                    return "a no es menor que b"
            else:
                return "La función no es diferenciable en b"
        else:
            return "La función no es diferenciable en a"
    else:
        return "La función no es convexa"


def teo1Bool(f,a,b,h):
    if convexaBool(f,a,b)==True: # Si f es convexa
        if diferenciableBool(f,a,h)==True: # Si f es diferenciable en a
            if diferenciableBool(f,b,h)==True: # Si f es diferenciable en b
                if a<b: # Si a<b
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

