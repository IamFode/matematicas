from definicionesC1.funcCreciente import funcCreciente

# Función creciente
class FuncionCreciente:

    def __init__(self,x,y,f):
        self.x = x
        self.y = y
        self.f = lambda x: eval(f)

    def funcionCreciente(self):
        return funcCreciente(self.x,self.y,self.f)

