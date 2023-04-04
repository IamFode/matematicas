"""
La raíz cuadrada positiva de la varianza recibe el nombre de la desviación estándar y se denota por
s=sqrt(varianza)
"""

# Importar definición 1.4
from def1_4 import varianza

def de(lista):
    var = varianza(lista)**0.5 #Raíz cuadrada
    return var

