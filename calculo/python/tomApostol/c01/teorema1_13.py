from defFuncCreciente import funcCreciente as funcCreciente

"""
TEOREMA 1.13
Supongamos f creciente en un intervalo cerrado [a,b]. Sea x_k = a+k(b-a)/n para k = 0,1,...,n.
Si I es un número cualquiera que satisface las desigualdades
(b-a)/n sum_{k=0}^{n-1} f(x_k) <= I <= (b-a)/n sum_{k=1}^{n} f(x_k)
para todo entero n>=1, entonces I=int_a^b f(x) dx.
"""

def teo1_13(a,b,func,n): # intervalo cerrado [a,b], función y n
    if n>=1: #n>=1
        f = lambda x: eval(func)
        if funcCreciente(a,b,f) == True:
            sum1, sum2 = 0, 0
            for k in range(n-1): # para k = 0,1,...,n
                x, x1 = a + k*(b-a)/n, a + (k+1)*(b-a)/n # Sea x_k = a+k(b-a)/n 
                sum1 += f(x)
                sum2 += f(x1)
            inf, sup = ((b-a)/n)*sum1, ((b-a)/n)*sum2
            if inf<sup:
                print("{} <= I <= {}".format(inf,sup)) #condición 1 <= I <= condición 2
                return (sup+inf)/2 # I=int_a^b f(x) dx
            else:
                print("error")
    else:
        print("n debe ser >= 1")

