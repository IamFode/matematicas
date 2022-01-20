# Library
from scipy.stats import uniform
from scipy.stats import expon

########################## Distribución uniforme ###############################

# Sea X una variable v.a. U(-1,1) a=-1 y b=1 así que loc=-1 y scale=b-a=1-(-1)=2
uniform.pdf(0.5,loc=-1,scale=2)

#función de distribución
uniform.ppf(0.5,loc=-1,scale=2)

# generación de elatorios uniforme
uniform.rvs(size=30,loc=-1,scale=2)


######################### Distribución exponencial #############################

# se pone scale=1./3 = 3
expon.pdf(0.0001,scale=1./3)
# función acumumulada
expon.cdf(0.5,scale=1./3)
expon.rvs(scale=1./3,size=10)
