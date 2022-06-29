import numpy as np

def teo1_13(a,b):
    sum1, sum2, n = 0, 0, 1000000

    f = lambda x: x**2

    for k in range(n-1):
        x, x1 = a + k*a/n, a + (k+1)*a/n
        sum1 += f(x)
        sum2 += f(x1)

    print("total menor: {}\nTotal mayor: {}".format(((b-a)/n)*sum1,((b-a)/n)*sum2))

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

teo1_13(a,b)

