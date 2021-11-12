
# fibonacci

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    sucesion = (((1+5**(1/2))/2)**n-((1-5**(1/2))/2)**n)/5**(1/2)
    return "Fibonacci: {} \nSucesión de Fibonacci: {}".format(a,sucesion)
