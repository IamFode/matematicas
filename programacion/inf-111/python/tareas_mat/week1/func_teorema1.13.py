import numpy as np

def teorema1_13(n,a,b):
    sum1 = 0
    sum2 = 0
    for k in range(0,n-1):
        x = a + k*(b-a)/n
        sum1 += x**2

    for k in range(1,n,1):
        x1 = a + k*(b-a)/n
        sum2 += x1**2

    print("Total menor: {} \nTotal mayor: {}".format(((b-a)/n)*sum1,((b-a)/n)*sum2))

n = int(input("Ingrese un número n entero grande: "))
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

teorema1_13(n,a,b)

