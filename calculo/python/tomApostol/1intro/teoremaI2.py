################ Teorema I2 ################
###### Posibilidad de la sustracción #######

import teoremas

class TeoremaI3(teoremas.Teoremas):

    def ejemteoI3(self):
        return f"Dado {a} y {b}, existe uno y sólo un x tal que {a}+{b-a}={b}. Este x se designa por {b-a}. En particular {-a} se escribe simplemente -({a}) y se denomina el negativo de {a}"

print(TeoremaI3(1,2).ejemteoI3())







