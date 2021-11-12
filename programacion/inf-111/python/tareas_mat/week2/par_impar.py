
# Todo número natural es par o impar

def parImpar(k):
    par,impar = [],[]
    for i in range(1,k+1):
        if i%2==0: 
            par.append(i)
        else:
            impar.append(i)
    return "Par: {} \nImpar: {}".format(par,impar)
