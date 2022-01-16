# library
from scipy.stats import binom

########################### Distribucion binomial ##############################

############## Función de probabilidad
def factorial(n):
  sum = 1
  for i in range(1,n+1):
    sum *= i
  return sum

def binomial(x,n,p):
  if isinstance(x,int) and x>=0:
    if p >= 0 and p <= 1:
      if isinstance(n,int):
        binom = (factorial(n)/(factorial(n-x)*factorial(x))) * p**x * (1-p)**(n-x) 
        print(binom) 
      else:
        print("n debe ser entero")
    else:
      print("p debe estar entre 0 y 1")
  else:
    print("x debe ser un número natural")
binomial(3,4,0.2)

# libraria stats
binom.pmf(3,4,0.2,loc=0)


