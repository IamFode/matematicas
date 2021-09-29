import numpy as np

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

sum1 = 0
sum2 = 0

n = 1000000

for k in range(0,n-1):
    x = a + k*(b-a)/n
    sum1 += x**2

for k in range(1,n,1):
    x1 = a + k*(b-a)/n
    sum2 += x1**2

print("total menor: {}".format(((b-a)/n)*sum1))
print("total mayor: {}".format(((b-a)/n)*sum2))
