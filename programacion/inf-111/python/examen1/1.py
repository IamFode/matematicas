n = 1 
count_menor = 0
count_mayor = 0

while n < 6:
    a = float(input("ancho: "))
    h = float(input("altura: "))
    sup = a*h
    if sup <= 5.2: 
        count_menor += 1
    else:
        count_mayor += 1
    n += 1

print("Superficie menores o iguales a 5.2: {} \n Superficie de pisos mayores a 5.2: {}".format(count_menor,count_mayor))
