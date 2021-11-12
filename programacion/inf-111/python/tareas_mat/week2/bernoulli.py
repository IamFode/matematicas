
# Desigualdad de Bernoulli
def Bernoulli(n,h):
    if h>-1:
        return "{} >= {}".format((1+h)**n,1+n*h)
    else:
        return "h debe ser mayor que -1"
