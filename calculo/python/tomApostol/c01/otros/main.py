import numpy as np

# Función creciente
class FuncionCreciente:

    def __init__(self,x,y,f,*args):
        self.a = a
        self.b = b
        self.f = lambda x: eval(f)
        self.args = args

    # Una función f se dice que es creciente en un conjunto S si f(x)<= f(y) para cada par de puntos
    # x e y de S con x<y.

    def funcCreciente(self): # Variables x,y con la función f y el conjunto S.
        if self.a<=self.b: #x<y
            for i in np.arange(self.a,self.b,0.3): 
                print(i)
                if not self.f(i)<=self.f(i+0.3): # f(x)<= f(y)
                    return False
                return True
        else:
            return False


# TEOREMA 1.13
class Teo1_13(FuncionCreciente):

    # llamar a funcion funcCreciente 
    if FuncionCreciente(self.a,self.b,self.f).funcCreciente() == True:

        # TEOREMA 1.13
        # Supongamos f creciente en un intervalo cerrado [a,b]. Sea x_k = a+k(b-a)/n para k = 0,1,...,n.
        # Si I es un número cualquiera que satisface las desigualdades
        # (b-a)/n sum_{k=0}^{n-1} f(x_k) <= I <= (b-a)/n sum_{k=1}^{n} f(x_k)
        # para todo entero n>=1, entonces I=int_a^b f(x) dx.

        def teorema1_13(self): # intervalo cerrado [a,b]
            #f = lambda x: eval(func)
            sum1, sum2, n = 0, 0, 10000 # n>=1
            for k in range(n-1): # para k = 0,1,...,n
                x, x1 = self.a + k*(self.b-self.a)/n, self.a + (k+1)*(self.b-self.a)/n # Sea x_k = a+k(b-a)/n 
                sum1 += self.f(x)
                sum2 += self.f(x1)
            inf, sup = ((self.b-self.a)/n)*sum1, ((self.b-self.a)/n)*sum2
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
print(Teo1_13(1,3,"x").teorema1_13())


