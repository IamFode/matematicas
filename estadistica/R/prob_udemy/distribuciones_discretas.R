################ Distribuciones notables discretas #############################
source("funciones.R")

#################### DISTRIBUCIÓN de BERNOULLI #################################
dbinom(0,size=1,prob = 0.25) # 0 probabilidad de fracaso (1-p)
dbinom(1,size=1,prob = 0.25) # 0 probabilidad de éxito p
rbinom(n=100,size=1, prob = 0.25)

######################### DISTRIBUCIÓN BINOMIAL ################################
# coheficiente binomial
choose(6,5)
choose(10,5)
choose(22,10)
# ejemplos
## P_X(x) = P(X<=0)
pbinom(0,size=10,prob = 0.25)
## P_X(x) = P(X<=4)
pbinom(4, size = 10, prob = 0.25)
## P_X(x) = P(X=0)
dbinom(0,size = 10, prob = 0.25)
## P(x=4)
dbinom(4, size = 10, prob = 0.25)
# Generacación de muestras aleatorias con R
set.seed(2019)
rbinom(100, size = 20, prob = 0.5) # random binom
#### ejemplo
# 100 bolas donde 40 son rojas y 60 blancas proceso n=10 y probabilidad de éxito 0.4
## probabilidad de sacar 4 rojas
### P(X=0)
dbinom(4,size = 10, prob = 0.4)
dist_binom(10,4,.4)
## probabilidad de sacar al menos 4 rojas
### P(X>=4) = 1-P(X<4) = 1 - P(x<=3)
pbinom(3,10,0.4)
1-pbinom(3,10,0.4)
pbinom(3,10,0.4,lower.tail = FALSE) #(1-función de distribución)
## probabilidad de sacar al menos 3 rojas
### P(x<3) = P(X<=2) = P(X=0) + P(X=1) + P(X=2)
dist_binom(10,0,.4) + dist_binom(10,1,.4) + dist_binom(10,2,.4)
## valor esperado de bolas rojas
10*.4
## desviación típica del número de bolas rojas

######################### DISTRIBUCIÓN GEOMÉTRICA  #############################
# ge(p=0.25)
  # P(X=0) = (1-0.25)^0 x 0.25^1 = 0.25
  dgeom(0,prob = 0.25)
  # P(X<=0) = 1 - (1-0.25)^{0+1} = 1 - 0.75 = 0.25
  pgeom(0,prob=0.25)
  # P(X<=4) = 1 - (1-0.25)^{4+1} = 1 - 0.75 = 1 - 0.75^5 = 0.7626
  pgeom(4,prob = 0.25)
  # una muestra aleatoria de tamaño 25 de una Ge(0.25)
  rgeom(n=25, prob = 0.25)
# gráfico 
par(mfrow = c(1,2))
x = c(0:10)
plot(x=x, y=dgeom(x,prob = 0.25),
  ylim=c(0,1), xlim = c(-1,11), xlab="x",
  main = "Función de probabilidad\n Ge(p=0.25)")
lines(x = rep(0:10, each = 2), y = aux, type = "h", lty = 2, col = "blue")
aux0 = dgeom(c(0:10),prob = 0.25)
ceros = rep(0,21)
ceros
aux = ceros
aux[2*(c(1:11))] <- aux0
curve(pgeom(x, prob = 0.25),
      xlim = c(-1,10), col = "blue",
      main = "Función de distribución\n Ge(p=0.25)")
par(mfrow=c(1,1))

################### Distribución binomial negativa #############################
# números binomiales negativos
choose(-6,4)

############################ Distribución Poisson ##############################

















