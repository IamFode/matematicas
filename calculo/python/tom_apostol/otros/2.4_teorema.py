import numpy as np

a = float(input("introducir a: "))

n = 1000000

if 0 < a and a < 1/2*np.pi and n>=1:

    def f(x):
        return np.cos(x)

    sum1, sum2 = 0, 0

    for k in range(n-1):
        x, x1 = k*a/n, (k+1)*a/n
        sum1 += f(x)
        sum2 += f(x1)

    print("total menor: {}".format((a/n)*sum1))
    print("total mayor: {}".format((a/n)*sum2))
    print(a/n*s)

else:

    print("a debe ser mayor que 0 y menor que pi/2 o n debe ser mayor o igual a 1")







