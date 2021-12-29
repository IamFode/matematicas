############################### Funciones ######################################

########################## Distribución binomial ##############################

# factorial
fact = function(x){
  mult <- 1
  while (x > 0) {
    mult <- mult*x
    x <- x-1
  }
  return(mult)
}

# coeficiente binomial
coe_binom <- function(n,k){
  return(fact(n)/(fact(k)*fact(n-k)))
}

coe_binom(10,2)

# función binomial binomial
func_binom = function(k,n,p){
  return(coe_binom(n,k)*p^{k}*(1-p)^{n-k})
}

func_binom(4,10,0.4)

################### Distribución binomial negativa #############################
varbn <- function(n) {
  return(n*(1-p)/p^2)
}


