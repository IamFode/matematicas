# Cuasivarianza

def cuasivar():
    vector = []
    sum1, sum2 = 0,0
    while n>0:
        x = float(input("Ingrese un número para el vector: "))
        vector.append(x)
        n -= 1
    for i in vector:
        sum1 += i**2
        sum2 += i 
    return (sum1 - (sum2**2/len(vector))) / (len(vector)-1)


