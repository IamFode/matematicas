"""
Para todos los números a y b se tiene
|a+b|<=|a|.|b|
"""

def teo1(a,b):
    return"Para todos los números {0} y {1} se tiene |{0}+{1}|<=|{0}|*|{1}|".format(a,b)

def teo1Bool(a,b):
    return abs(a+b)<=abs(a)*abs(b)

