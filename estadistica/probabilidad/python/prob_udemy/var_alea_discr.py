
# Función de Esperanza matemática de una variable aleatoria discreta. 
def esper_discr(n):
    s = 0
    while n != 0:
        V = int(input("Ingrese la variable aleatoria discreta: "))
        p = float(input("Ingrese el valor de la probabilidad: "))
        s += n * p
        n -= 1
    return s

# sumas parciales desde el término n_0 al n de una progresión geométrica.


