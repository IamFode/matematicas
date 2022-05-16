
source("funciones.R")
################################## factorial ###################################
fact <- function(x){
  if (x==0){
    return(1)
  }else{
    sum = 1
    for (i in 1:x){
      sum = sum * i
    }
    return(sum)
  }
}

############################ Distribución Binomial #############################

# Función de probabilidad
func_binom <- function(x,n,p){
  return(fact(n) / (fact(n-x)*fact(x)) * p^x * (1-p)^(n-x))
}

# función acumulada
acum_binom <- function(x,n,p){
  sum <- 0
  for (i in 0:x){
    sum = sum + (fact(n) / (fact(n-i)*fact(i)) * p^i * (1-p)^(n-i))
  }
  return(sum)
}


# función de probabilidad de la distribución puntual o Bernoulli
dist_bernoulli <- function(x,p){
  if (x>=0){
    return(p^x * (1-p)^{1-x})
  }else{
    return("x debe ser mayor o igual a 0")
  } 
}

# esperanza matemática
Es_binom <- function(n,p) n*p

# varianza
var_binom <- function(n,p) n*p*(1-p)

######################## Distribución de Poisson ###############################

# función de probabilidad
func_poisson <- function(x,lambda){
  if (lambda > 0 & x>0 & x%%1==0){
  return((exp(-lambda)*lambda^x)/fact(x))
  }else{
    return("lambda debe ser mayor a 0 o x intero mayor o igual a cero")
  }
}

# función acumulada
acum_poisson <- function(x,lambda){
  if (lambda > 0 & x>0 & x%%1==0){
    sum = 0
    for (i in 0:x){
      sum = sum + (exp(-lambda)*lambda^i)/fact(i)
    }
  return(sum)
  }else{
    return("lambda debe ser mayor a 0 o x intero mayor o igual a cero")
  }
}

######################## Distribución hipergeométrica ##########################

# función de probabilidad
func_hiper = function(x,N,n,k){
  if(x>=0 & x<=k & n<=N-k+x){
    return((perm_sin_orden(k,x)*perm_sin_orden(N-k,n-x))/perm_sin_orden(N,n))
  }
  else{
    return(0)
  }
}

x <- 1 # variable a determinar
N <- 12 # Población
n <- 3 # muestra
k <- 5 # casos exitosos
func_hiper(x,N,n,k)
dhyper(x = x,m = k,n = N-k,k = n)

# función acumulada
acum_hiper = function(x,N,n,k){
  sum = 0
  for(i in 0:x){
    sum=sum+((perm_sin_orden(k,i)*perm_sin_orden(N-k,n-i))/perm_sin_orden(N,n))
  }
  return(sum)
}

x <- 1 # variable a determinar
N <- 12 # Población
n <- 3 # muestra
k <- 5 # casos exitosos
acum_hiper(x,N,n,k)
phyper(q=x,m=k,n=N-k,k=n)

