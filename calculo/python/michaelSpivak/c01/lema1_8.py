"""
Lema 1.8

Si a<b, entonces a+c<b+c
"""

def lema1_8(a, b, c):
    return "Si {0}<{1}, entonces {0}+{2}<{1}+{2}".format(a,b,c)

def lema1_8Bool(a, b, c):
    if a < b:
        return a + c < b + c
    else:
        return False
