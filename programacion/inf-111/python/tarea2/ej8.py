# variable de entrada
n = int(input("Ingrese un número entre 0 y 1000: "))

#variable suma igual a 0
suma = 0 

# sumando los dígitos 
while n!=0:
    ext = n%10
    suma += ext
    n = n//10

# Imprimir 
print("La suma de los dígitos es: ",suma)
