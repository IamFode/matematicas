# numerical derivate of a function
f = lambda x: x**2
def derivada(x,h=1e-7):
    return (f(x+h)-f(x))/h

print(derivada(1))
