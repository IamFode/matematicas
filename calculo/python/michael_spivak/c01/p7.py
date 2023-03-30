"""
Para todo número a!=0, existe un número a**(-1) tal que
a*a**(-1)=a**(-1)*a=1.
"""

def prop7(a):
    if a != 0:
        return "Para todo número {0}!=0, existe un número {0}**(-1) tal que \n {0}*{0}**(-1)={0}**(-1)*{0} = 1".format(a)
    else:
        return "a debe ser distinto de 0"

def prop7Num(a):
    if a!=0: # condición a!=0
        mult1 = a*a**(-1) # multiplicación de la derecha de la ecuación
        mult2 = a**(-1)*a # multiplicación de la izquierda de la ecuación
        print(mult1,"=",mult2,"=",1) # imprime las multiplicaciones
        return 1 # retorna 1 si se cumple la condición
    else:
        return "a debe ser distinto de 0"

