
# Desigualdad de Schwarz

def Schwarz(n):
    sum1, sum2, sum3 = 0,0,0
    for i in range(1,n+1):
        sum1+=i * i**2
        sum2+=i**2
        sum3+=(i**2)**2
    return "{} <= {}".format(sum1,((sum2)**(1/2))*((sum3)**(1/2)))
