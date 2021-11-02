import math

def area(x):
    return (5*x**2) / (4*math.tan(math.pi / 5))

lado = float(input("Ingrese el lado: "))

print("El área del pentágono es: {}".format(area(lado)))
