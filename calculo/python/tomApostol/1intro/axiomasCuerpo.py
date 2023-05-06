##############################################################
################## Axiomas de cuerpo #########################
##############################################################

class Axiomas:
    def __init__(self,x,y=None,z=None):
        self.x = x
        self.y = y
        self.z = z

class ejemaxiom(Axiomas):
    # Propiedad conmutativa
    def conmutativa(self):
        return f"Propiedad conmutativa: {self.x} + {self.y} = {self.y} + {self.x} = {self.x+self.y}, {self.x} * {self.y} = {self.y} * {self.x} = {self.x*self.y}"
    # Propiedad asociativa
    def asociativa(self):
        return f"Propiedad asociativa: ({self.x} + {self.y}) + {self.z} = {self.x} + ({self.y} + {self.z}) = {self.x+self.y+self.z}, ({self.x} * {self.y}) * {self.z} = {self.x} * ({self.y} * {self.z}) = {self.x*self.y*self.z}"
    # Propiedad distributiva
    def distributiva(self):
        return f"Propiedad distributiva: {self.x} * ({self.y} + {self.z}) = {self.x} * {self.y} + {self.x} * {self.z} = {self.x*(self.y+self.z)}"
    # Existecia de elementos neutros
    def neutro(self):
        return f"Existencia de elementos neutros: {self.x} + 0 = {self.x}, {self.x} * 1 = {self.x}"
    # Existencia de negativos
    def negativo(self):
        return f"Existencia de negativos: {self.x} + (-{self.x}) = 0"
    # Existencia de recíproco
    def reciproco(self):
        if self.x != 0:
            return f"Existencia de recíproco: {self.x} * {1/self.x} = 1"
        else:
            return "No existe recíproco"

class Axioma(Axiomas):

    def sum(self):
        return self.x + self.y

    def prod(self):
        return self.x * self.y

    def asocia(self):
        return self.x + (self.y + self.z)

    def distr(self):
        return self.x * (self.y + self.z)

    def neutro(self):
        return self.x + 0

    def neg(self):
        return self.x + (-self.x)

    def recip(self):
        if self.x != 0:
            return self.x * (1/self.x)
        else:
            return "No existe el recíproco"

##############################################################

