
########################### Distribución binomial ##############################
factorial <- function(n){
  sum <- 1 
  for (i in 1:n){
    sum <- sum * i
  }
  return(sum)
} 
binomial <- function(x,n,p){
  if(x%%2 == 0){
    return(factorial(n)/(factorial(n-x)*factorial(x))*p^(x)*(1-p)^(n-x))
  }else{
    return("x debe ser un número natural")
  }
}
binomial(4,10,0.1)

dbinom(4,10,0.1)
