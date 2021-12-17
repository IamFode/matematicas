import numpy as np

def teo1_13(a,b):
    sum1, sum2, n = 0, 0, 1000000

    for k in range(0,n-1):
        x = a + k*(b-a)/n
        sum1 += x**2

    for k in range(1,n):
        x1 = a + k*(b-a)/n
        sum2 += x1**2

    print("total menor: {}\nTotal mayor: {}".format(((b-a)/n)*sum1,((b-a)/n)*sum2))

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

teo1_13(a,b)
