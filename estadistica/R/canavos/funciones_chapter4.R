
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

1-acum_binom(2,10,0.3)
func_binom(5,10,0.3)

