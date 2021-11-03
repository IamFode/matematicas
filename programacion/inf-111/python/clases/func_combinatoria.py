# write the combinatorial of n over m with for loop
def combinatoria(n, m):
    r = 1
    for i in range(m):
        r *= (n - i)
        r /= (i + 1)
    return r

# input n and k
n = int(input("n: "))
m = int(input("k: "))

# print the result
print(combinatoria(n, m))

