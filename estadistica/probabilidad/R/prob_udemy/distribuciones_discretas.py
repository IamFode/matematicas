from scipy.stats import binom

# binom.pmf()(k,n,p,loc) = binom.pmf(k-loc,n,p)

# F_X(0) = P(X<=0) y $f_X(X<=4)
binom.cdf(0,n=10,p=.25) # distribuciones acumiladas cdf
binom.cdf(4,n=10,p=.25)

 # P(X=0) y P(X=4)
 binom.pmf(0,n=10,p=0.25) #distrubciones iguales pmf
 binom.pmf(4,n=10,p=0.25)
 
 # distribución binomial (rvs)
 binom.rvs(n=20,p=0.25,size=100)
 
 
#### ejemplo
# 100 bolas donde 40 son rojas y 60 blancas proceso n=10 y probabilidad de éxito 0.4
## probabilidad de sacar 4 rojas
## probabilidad de sacar al menos 4 rojas
## probabilidad de sacar al menos 3 rojas
## valor esperado de bolas rojas
print("E(X) = {m}".format(m=binom.stats(n=10, p=.4, moments = 'm')))
## desviación típica del número de bolas rojas
print("Var(X) = {v}".format(v=binom.stats(n=10, p=.4, moments = 'v')))
