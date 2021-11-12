
# función de coheficiente binomial

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    t = 1
    for i in range(min(k, n - k)):
        t = t * (n - i) // (i + 1)
    return t
