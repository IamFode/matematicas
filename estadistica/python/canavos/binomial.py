from factorial import factorial

def func_binomial(x,n,p):
    return factorial(n) / (factorial(n-x)*factorial(x)) * p**x * (1-p)**(n-x)

x = int(input("Introducir un x (éxito) entero: "))
n = int(input("Introducir n ensayos: ")) 
p = float(input("Introducir probabilidad de éxito: "))

print(func_binomial(x,n,p))


