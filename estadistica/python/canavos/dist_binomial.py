from factorial import factorial

def dist_binomial(x,n,p):
    sum = 0
    for i in range(x+1):
        sum += factorial(n) / (factorial(n-i)*factorial(i)) * p**i * (1-p)**(n-i)
    return sum

x = int(input("Introducir un x (éxito) entero: "))
n = int(input("Introducir n ensayos: ")) 
p = float(input("Introducir probabilidad de éxito: "))

print(dist_binomial(x,n,p))
