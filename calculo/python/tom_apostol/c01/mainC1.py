from timeit import default_timer as timer

class Def_c1:
    def __init__(self,a,b,f):
        self.a = a
        self.b = b
        self.f = lambda x: eval(f)
        #self.polinomial = lambda x: eval(f**p)

    def funcionCreciente(self):
        return funcCreciente(self.a,self.b,self.f)



# imprimir funcfionDecreciente
print(Def_c1(1,3,"x**2").funcionCreciente())


"""
inicio = timer()
print(teo1_13(1,3,"x**2+1"))
fin = timer()
print("Tiempo de ejecución: {}".format(fin-inicio))
"""
