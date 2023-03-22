import c1Def 
from teoremasC1.teorema1_13 import teo1_13

FuncionCreciente = c1Def.FuncionCreciente

# TEOREMA 1.13
class Teo1_13(FuncionCreciente):
    def __init__(self,a,b,f):
        self.a = a
        self.b = b
        self.f = lambda x: eval(f)

    if FuncionCreciente.funcionCreciente(self) == True:
        def teorema1_13(self): # intervalo cerrado [a,b]
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


# TEOREMA 1.15
class Teo1_15:
    def teorema1_15(self):
        return teo1_15(self.b,self.p)


# imprimir teorema1_13
print(Teo1_13(1,3,"x**2+1").teorema1_13())
