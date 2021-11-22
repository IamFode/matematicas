# función media aritmética, media cuadrática y media aritmética.
def promedios(lista):
    sum_arit, sum_cuad, sum_armo = 0,0,0
    
    ## loop for para sumar los valores de la lista
    for i in lista:
        sum_arit += i
        sum_cuad += i**2
        sum_armo += i**(-1)
    
    aritmetica = sum_arit / len(lista)
    cuadratica = (sum_cuad / len(lista))**(1/2)
    armonica = (sum_armo / len(lista))**(-1)
    return "Media aritmética: {:.2f} \nMedia cuadrática:{:.2f} \nMedia armónica: {:.2f}".format(aritmetica, cuadratica, armonica)

list_ = list(map(float, input("Agregar lista: ").strip().split()))
print(promedios(list_))


