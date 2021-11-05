
def teorema1_15(n,b,p):

    n_1, n_2, int = 0, 0, (b**(p+1))/(p+1)

    for k in range(0,n):
        n_1 += ((k*b)/n)**p

    for t in range(1,n+1):
        n_2 += ((t*b)/n)**p

    print("{} < {} < {}".format((b/n) * n_1, int, n_2*(b/n)))


n = int(input("Ingrese un número entero n>0 grande: "))
b = float(input("Ingrese un número b: "))
p = float(input("Ingrese un número p: "))

teorema1_15(n,b,p)
