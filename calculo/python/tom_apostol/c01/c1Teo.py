import c1Def 
from teoremasC1.teorema1_13 import teo1_13

FuncionCreciente = c1Def.FuncionCreciente

# TEOREMA 1.13
class Teo1_13(FuncionCreciente):

    def teorema1_13(self):
        if FuncionCreciente.funcionCreciente(self) == True:
            return teo1_13(self.x,self.y,self.f)


# TEOREMA 1.15
class Teo1_15:
    def teorema1_15(self):
        return teo1_15(self.b,self.p)


# imprimir teorema1_13
print(Teo1_13(1,2,'x**2').teorema1_13())
