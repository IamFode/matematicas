#### Clase padre de teoremas ####

class Teoremas:
    def __init__(self,a,b=None,c=None,d=None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # Ejemplo del Teorema I.1
    def ejemteoI1(self):
        if self.b == self.c:
            return f"LEY DE SIMPLIFICACIÓN PARA LA SUMA. Si {self.a}+{self.b}={self.a}+{self.c}, entonces {self.b}={self.c}. (En particular esto prueba que el número 0 del axioma 4 es único.)"
        else:
            return "No se cumple la condición"

    # Teorema I.1 booleano y numerico
    def boolTeoI1(self):
        if self.b == self.c:
            return self.b == self.c
        else:
            return "No se cumple la condición"

    def numTeoI1(self):
        if self.b == self.c:
            return self.b
        else:
            return "No se cumple la condición"

    # Ejemplo del Teorema I.2
    def ejemteoI2(self):
        return f"Dado {self.a} y {self.b}, existe uno y sólo un x tal que {self.a}+x={self.b}. Este x se designa por {self.b}-({self.a}). En particular -{self.a} se escribe simplemente {-self.a} y se denomina el negativo de {self.a}"


print(Teoremas(-1,2).ejemteoI2())

