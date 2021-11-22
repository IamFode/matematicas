# norma de un vector
def norma(v):
    return (v[0]**2 + v[1]**2)**0.5

# entrada
v = list(map(float,input("Introducir vector v: ").strip().split()))

# salida
print(norma(v))
