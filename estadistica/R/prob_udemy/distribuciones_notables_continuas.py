
########################## Distribución uniforme ###############################
from scipy.stats import uniform
# Sea X una variable v.a. U(-1,1) a=-1 y b=1 así que loc=-1 y scale=b-a=1-(-1)=2
uniform.pdf(0.5,loc=-1,scale=2)

#función de distribución
uniform.ppf(0.5,loc=-1,scale=2)

# generación de elatorios uniforme
uniform.rvs(size=30,loc=-1,scale=2)


######################### Distribución exponencial #############################
from scipy.stats import expon
# se pone scale=1./3 = 3
expon.pdf(0.0001,scale=1./3)
# función acumumulada
expon.cdf(0.5,scale=1./3)
expon.rvs(scale=1./3,size=10)


############################# Distribución normal ##############################
from scipy.stats import norm
# X - N(mu=1,sigma=2) función de densidad f_x(2):
norm.pdf(2,loc=1,scale=2)
# función de distribución F_X(2)=P(X<=2)
norm.cdf(2,loc=1,scale=2)
# cuantil x_0.95 P(X<=x_0..95) = 0.95 
norm.ppf(0.95,loc=1,scale=2)
# generación aleatoria de valores según $X$ como
norm.rvs(loc=1,scale=2,size=5)
