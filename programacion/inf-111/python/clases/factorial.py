
# factorial function with for loop
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# input
n = int(input("Ingresar un número: "))

# print factorial and input n
print("Factorial de", n, "es:", factorial(n))
