# varianza 
def var(vector):
    if len(vector) == 0:
        return 0
    else:
        mean = sum(vector) / len(vector)
        return sum([(x - mean) ** 2 for x in vector]) / len(vector)

vector = list(map(float,input("Introducir vector: ").strip().split()))
print("La varianza es: ", var(vector))



