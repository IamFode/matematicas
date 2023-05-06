##################### Teorema I.1 ####################
######### LEY DE SIMPLIFICACIÓN PARA LA SUMA #########

import teoremas

class ejemteoI1(teoremas.Teoremas):
    def ejemteoI1(self):
        if self.b == self.c:
            return f"LEY DE SIMPLIFICACIÓN PARA LA SUMA. Si {self.a}+{self.b}={self.a}+{self.c}, entonces {self.b}={self.c}. (En particular esto prueba que el número 0 del axioma 4 es único.)"
        else:
            return "No se cumple la condición"


class TeoremaI1(teoremas.Teoremas):

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

class TeoremaI3(teoremas.Teoremas):

    def ejemteoI3(self):
        return f"Dado {a} y {b}, existe uno y sólo un x tal que {a}+{b-a}={b}. Este x se designa por {b-a}. En particular {-a} se escribe simplemente -({a}) y se denomina el negativo de {a}"


print(TeoremaI3(1,2).ejemteoI3())
