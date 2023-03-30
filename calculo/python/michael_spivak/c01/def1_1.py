"""
Consideremos a-b como una abreviación de a+(-b)
"""

def def1_1(a,b):
    return "{0}-{1} = {0}+(-{1})".format(a,b)

def def1_1Num(a,b):
    sumader = a-b
    sumaizq = a+(-b)
    print("{0} = {1}".format(sumader,sumaizq))
    return sumader
