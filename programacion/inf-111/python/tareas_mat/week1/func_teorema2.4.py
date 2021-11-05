import numpy as np

def teorema2_4(n,a):

    sum1 = 0 
    sum2 = 0

    for k in range(0,n-1):
        x =  k*a/n
        sum1 += np.cos(x) 

    for k in range(1,n,1):
        x1 =  k*a/n
        sum2 += np.cos(x1) 

    print("Total menor: {} \nTotal mayor: {}".format((a/n)*sum1,(a/n)*sum2))

n = int(input("introducir un número n>0 grande: "))
a = float(input("introducir a: "))

teorema2_4(n,a)
