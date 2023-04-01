"""
LEMA 1.3

Si ab=0. Entonces, a=0 o b=0.
"""

def lema1_3(a,b):
    if a*b == 0: # Si ab=0
        return "Si {0}*{1}=0. Entonces, {0}=0 o {1}=0.".format(a,b)
    else:
        return "a y b no son cero."


