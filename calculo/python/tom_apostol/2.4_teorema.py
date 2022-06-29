import numpy as np

a = float(input("introducir a: "))

sum1, sum2 = 0, 0

def f(x):
    return np.cos(x)

n = 1000000

for k in range(n-1):
    x, x1 = k*a/n, (k+1)*a/n
    sum1 += f(x)
    sum2 += f(x1)


print("total menor: {}".format((a/n)*sum1))
print("total mayor: {}".format((a/n)*sum2))
