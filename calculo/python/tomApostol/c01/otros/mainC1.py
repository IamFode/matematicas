from timeit import default_timer as timer
from teoremasC1.teorema1_13 import teo1_13
from teoremasC1.teorema1_15 import teo1_15
from definicionesC1.funcCreciente import funcCreciente


class Def_c1:
    def __init__(self,a,b,f,*args):
        self.a = a
        self.b = b
        self.f = lambda x: eval(f)
        self.args = args

    def funcCreciente(self):
        return funcCreciente(self.a,self.b,self.f)


class Teo_c1(Def_c1):

    def teorema1_13(self):
        # Heredar atributos de la clase padre
        return teo1_13(self.a,self.b,self.f)


    def teorema1_15(cls):
        return teo1_15(self.b,self.p)



print(Def_c1(1,3,"x**2+1").funcCreciente())
print(Teo_c1(1,3).teorema1_15())


"""
inicio = timer()
print(teo1_13(1,3,"x**2+1"))
fin = timer()
print("Tiempo de ejecución: {}".format(fin-inicio))
"""
