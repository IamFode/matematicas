
#################### Distribución geométrica con python ########################
#Veamos los cálculos básicos con python para la distribución geométrica Ge(p=.25)

# libraria
from scipy.stats import geom

# P(X=0) = (1-0.25)^0 0.25^1 = 0.25
geom.pmf(0,p=0.25,loc=-1)

# P(X<=0) = 1 - (1-0.25)^(0+1) = 1-0.75 = 0.25
geom.cdf(0,p=0.25,loc=-1)

#P(X <= 4) = 1-(1-0.25)^{4+1} = 1-0.75^5 = 0.7626953
geom.cdf(4,p=0.25,loc=-1)

# Una muestra de tamaño 20 de una Ge(0.25) 
geom.rvs(p=0.25,size=20,loc=-1)
# Fallariamos 4 veces antes del primer éxito y así sucesivamente.

#### Ejercicio ####
# Que probabilidad son las que calcula el siguiente código y qué tipo de variables
# geométricas son?

geom.cdf(range(5),p=0.3,loc=0) # loc = 0, es el número de intentos hasta el éxito

geom.cdf(range(5),p=0.3,loc=-1) # número de fracasos antes del primer éxito

# 
geom.stats(p=0.25,loc=0,moments='mv')

geom.stats(p=0.25,loc=-1,moments='mv')



