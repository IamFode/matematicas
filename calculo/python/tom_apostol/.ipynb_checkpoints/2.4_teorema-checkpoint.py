
import numpy as np

a = float(input("introducir a: "))

sum1 = 0
sum2 = 0

n = 1000000

for k in range(0,n-1):
    x =  k*a/n
    sum1 += np.cos(x) 

for k in range(1,n,1):
    x1 =  k*a/n
    sum2 += np.cos(x1) 

print("total menor: {}".format((a/n)*sum1))
print("total mayor: {}".format((a/n)*sum2))
