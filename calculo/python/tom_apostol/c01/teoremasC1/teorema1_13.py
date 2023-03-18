
"""
TEOREMA 1.13
Supongamos f creciente en un intervalo cerrado [a,b]. Sea x_k = a+k(b-a)/n para k = 0,1,...,n.
Si I es un número cualquiera que satisface las desigualdades
(b-a)/n sum_{k=0}^{n-1} f(x_k) <= I <= (b-a)/n sum_{k=1}^{n} f(x_k)
para todo entero n>=1, entonces I=int_a^b f(x) dx.
"""

def teo1_13(a,b,f): # intervalo cerrado [a,b]
    #f = lambda x: eval(func)
    sum1, sum2, n = 0, 0, 10000 # n>=1
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


# código alternativo
def teo1_13_alter(a,b,func):
    sum1, sum2, n = 0, 0, 20000
    f = lambda x: eval(func)
    sum1 = sum([f(a + k*(b-a)/n) for k in range(n-1)])
    sum2 = sum([f(a + (k+1)*(b-a)/n) for k in range(n-1)])
    inf, sup = ((b-a)/n)*sum1, ((b-a)/n)*sum2
    print("inf: {}\nsup: {}".format(inf,sup))
    return (sup+inf)/2
