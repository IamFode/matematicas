from scipy.stats import binom
from scipy.stats import geom
import numpy as np
import matplotlib.pyplot as plt

# binom.pmf()(k,n,p,loc) = binom.pmf(k-loc,n,p)
# F_X(0) = P(X<=0) y $f_X(X<=4)
binom.cdf(0,n=10,p=.25) # distribuciones acumiladas cdf
binom.cdf(4,n=10,p=.25)
 # P(X=0) y P(X=4)
 binom.pmf(0,n=10,p=0.25) #distrubciones iguales pmf
 binom.pmf(4,n=10,p=0.25)
 
######################### DISTRIBUCIÓN BINOMIAL (rvs) ##########################
binom.rvs(n=20,p=0.25,size=100)
# ejemplo
# 100 bolas donde 40 son rojas y 60 blancas proceso n=10 y probabilidad de éxito 0.4
## probabilidad de sacar 4 rojas
## probabilidad de sacar al menos 4 rojas
## probabilidad de sacar al menos 3 rojas
## valor esperado de bolas rojas
print("E(X) = {m}".format(m=binom.stats(n=10, p=.4, moments = 'm')))
## desviación típica del número de bolas rojas
print("Var(X) = {v}".format(v=binom.stats(n=10, p=.4, moments = 'v')))
#gráfico
n, p = 10, 0.25
x = np.arange(binom.ppf(0.01, n, p),binom.ppf(0.99, n, p))
fig =plt.figure(figsize=(5, 2.7))
ax = fig.add_subplot(1,2,1)
ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
for tick in ax.xaxis.get_major_ticks():
  tick.label.set_fontsize(5)
for tick in ax.yaxis.get_major_ticks():
  tick.label.set_fontsize(5) 
ax = fig.add_subplot(1,2,2)
ax.plot(x, binom.cdf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.cdf(x, n, p), colors='b', lw=5, alpha=0.5)
for tick in ax.xaxis.get_major_ticks():
  tick.label.set_fontsize(5)
for tick in ax.yaxis.get_major_ticks():
  tick.label.set_fontsize(5)
fig.suptitle('Distribucion Binomial')
plt.show()
########################### DISTRIBUCIÓN GEOMÉTRICA ############################
# geom.pmf(x,p,loc=-1) = geom.pmf(x-1,p,loc=0) 
        ## loc= -1 el número de fracasos antes del 1er éxito
        ## loc = 0 la probabilidad del primer éxito
# ge(p=0.25)
  # P(X=0) = (1-0.25)^0 x 0.25^1 = 0.25
geom.pmf(0,p=0.25,loc=-1) 
  # P(X<=0) = 1 - (1-0.25)^{0+1} = 1 - 0.75 = 0.25 función de distribución
geom.cdf(0,p=0.25,loc=-1)
  # P(X<=4) = 1 - (1-0.25)^{4+1} = 1 - 0.75 = 1 - 0.75^5 = 0.7626 
geom.cdf(4,p=0.25,loc=-1)          
  # una muestra aleatoria de tamaño 25 de una Ge(0.25)
geom.rvs(p=.25,size=20,loc=-1) 
#cálculo de esperanza y varianza
geom.stats(p=.25, loc=0, moments="mv")
geom.stats(p=.25, loc=-1, moments="mv")
# gráfico 
p = .25
x = np.arange(geom.ppf(0.01, p), geom.ppf(0.99, p))
fig = plt.figure(figsize=(5,2.7))
ax = fig.add_subplot(1,2,1)
ax.plot(x, geom.pmf(x, p), "bo", ms=5, label="geom pmf")
ax.vlines(x, 0, geom.pmf(x, p), colors='b', lw=2, alpha=.5)
for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(5)
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(5)
ax = fig.add_subplot(1,2,2)
ax.plot(x, geom.cdf(x, p), 'bo', ms=5, label="geom pmf")
ax.vlines(x, 0, geom.cdf(x, p), colors = 'b', lw=2, alpha=.5)
for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(5)
for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(5)
fig.suptitle("Distribución Geométrica")
plt.show()
