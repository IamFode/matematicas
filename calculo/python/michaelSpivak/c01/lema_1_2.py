"""
Si ab = ac y a!=0, entonces b = c
"""

def lema1_2(a, b, c):
    if a != 0:
        if a * b == a * c:
            return "Si {0}{1}={0}{2} y {0}!=0, entonces {1} = {2}".format(a,b, c)
        else:
            return "{0}*{1} es distinto de {0}*{2}".format(a,b, c)
    else:
        return "a = 0"

def lema1_2Bool(a, b, c):
    if a != 0: # Si a es diferente de 0
        if a * b == a * c: # Si ab es igual a ac
            return True
        else:
            return False
    else:
        return False

