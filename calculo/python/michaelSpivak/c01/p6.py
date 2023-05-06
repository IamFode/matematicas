"""
Si a es cualquier número, entonces
a*1=1*a=a
"""

def prop6(a):
    return "Si {0} es  cualesquier número, entonces {0}*1 = 1*{0}={0}".format(a)

def prop6Num(a):
    print("{0}*{1} = {1}*{0} = {0}".format(a,1))
    return a

print(prop6Num(2))

