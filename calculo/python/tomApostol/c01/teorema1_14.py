from defFuncDecreciente import funcDecreciente
"""
Supongamos f decreciente en [a,b]. Sea x_k=c+k(b-a)/n para k=0,1,...,n. Si I es un número cualquiera
que satisface las desigualdades
(b-a)/n \sum_{k=1}^n f(x_k) <= I <= (b-a)/2 \sum_{k=1}^{n-1} f(x_k)
para todo entero n>=1, entonces I=\int_a^b f(x) dx.
"""

def teo1_14(a,b,func,n): # intervalo cerrado [a,b], función y n
    if n>=1: #n>=1
        f = lambda x: eval(func)
        if funcDecreciente(a,b,f) == True:
            sum1, sum2 = 0, 0
            for k in range(n-1): # para k = 0,1,...,n
                x, x1 = a + k*(b-a)/n, a + (k+1)*(b-a)/n # Sea x_k = a+k(b-a)/n 
                sum1 += f(x)
                sum2 += f(x1)
            sup, inf = ((b-a)/n)*sum1, ((b-a)/n)*sum2
            if inf<sup:
                print("{} <= I <= {}".format(inf,sup)) #condición 1 <= I <= condición 2
                return (sup+inf)/2 # I=int_a^b f(x) dx
            else:
                print("error")
    else:
        print("n debe ser >= 1")

print(teo1_14(1,3,'1/x',55000))
