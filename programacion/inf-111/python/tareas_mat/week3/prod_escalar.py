# Producto escalar
def scalar_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

# entrada 
v1 = list(map(float,input("Introducir vector v1: ").strip().split()))
v2 = list(map(float,input("Introducir vector v2: ").strip().split()))

# salida
print(scalar_product(v1,v2))
