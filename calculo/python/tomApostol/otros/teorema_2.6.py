import numpy as np
import sympy as sp

def teo2_6(a,b,f):
    sum1, sum2, n = 0, 0, 1000000

    f = sp.Symbol('f')

    for k in range(0,n-1):
        x = a + k*(b-a)/n
        sum1 += f 
        res1 = (b-a)/n * sum1

    for k in range(1,n):
        x1 = a + k*(b-a)/n # genera los puntos de x 
        sum2 += f 
        res2 = (b-a)/n * sum2

    print("total menor: {}\nTotal mayor: {}".format(res1, res2))


a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
func = input()

teo2_6(a,b,func)

