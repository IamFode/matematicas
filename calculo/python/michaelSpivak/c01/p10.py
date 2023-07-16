"""
PROPIEDAD 10

Para todo número $a$ se cumple una y sólo una de las siguientes igualdades:
a=0
a pertenece al conjunto P
-a pertenece al conjunto P
"""

def prop10(a):
    if a == 0:
        print("{} = 0".format(a))
    elif a in P:
        print("{} pertenece al conjunto P".format(a))
    elif -a in P:
        print("{} pertenece al conjunto P".format(-a))
    else:
        return False
    
print(prop10(0))
