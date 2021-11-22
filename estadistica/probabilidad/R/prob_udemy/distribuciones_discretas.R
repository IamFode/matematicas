################ Distribuciones notables discretas #############################
source("funciones.R")
################ Distribución Bernoulli

dbinom(0,size=1,prob = 0.25) # 0 probabilidad de fracaso (1-p)
dbinom(1,size=1,prob = 0.25) # 0 probabilidad de éxito p
rbinom(n=100,size=1, prob = 0.25)

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


###################### Distribución geométrica
