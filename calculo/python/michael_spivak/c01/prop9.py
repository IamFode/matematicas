"""
(P) LEY DISTRIBUTIVA

Si a, b y c son números cualesquiera, entonces
a(b + c) = ab + ac
"""

def prop9(a, b, c):
    return "Si {0}, {1} y {2} son números cualesquiera, entonces {0}({1} + {2}) = {0}*{1} + {0}*{2}".format(a, b, c)

def prop9Num(a, b, c):
    sumder = a*(b + c)
    sumizq = a*b + a*c
    print(sumder,"=",sumizq)
    return sumder

