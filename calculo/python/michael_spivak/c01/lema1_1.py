"""
Si un número x satisface a+x=a para cierto a, entonces es x=0.
"""

def lema1_1(x,a):
    if x+a==a:
        return "Si un número {0} satisface {1}+{0}={1} para cierto {1}, entonces es x={0}".format(x,a)
    else:
        return "x no es 0"

def lema1_1Num(x,a):
    if x+a==a:
        return 0
    else:
        return "x no es 0"

