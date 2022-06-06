################################################################################
################################ CANAVOS  ######################################

#-------------------------------------------------------------------------------

#############################  CAPÍTULO 1  #####################################
######################  ESTADÍSTICA DESCRIPTIVA  ###############################
################################################################################

## moda
moda = function(x){
  sort(table(x),TRUE)[1]
}

## Varianza de observaciones con error mínimo
varianza = function(x){
  n <- 0
  sq <- 0
  for (i in x){
    n <- n+i
    sq <- sq+i^2
  }
  return( (sq-(n^2/length(x))) / (length(x)-1) )
}

## Desviación media
DM = function(x){
  suma <- 0
  for (i in x){
    suma <- suma + abs(i-mean(x))
  }
  return(suma/length(x))
}

## Desviación mediana
DMed = function(x){
  suma <- 0
  for (i in x){
    suma <- suma + abs(i-median(x))
  }
  return(suma/length(x))
}


#############################  CAPÍTULO 2  #####################################
######################  CONCEPTOS DE PROBABILIDAD  #############################
################################################################################

# Factorial
fact = function(num){
  fac = 1
  if(num < 0) {
    print("No existe para número negativos")
  } else if(num == 0) {
    return(as.numeric("0"))
  } else {
    for(i in 1:num) {
      fac = fac * i
    }
    return(fac)
  }
}

#Permutaciones sin repetición 
# (luego que sea el elegido la primera persona ya no se toma en cuenta)
## factorial(n)
# permutations(n= 5, r= 5, v=x, repeats.allowed = FALSE)

# variación con repetición
#se puede repetir los elementos (bebidas) y donde no se consideran todos los elementos 
# (existen cuatro posibles bebidas pero solo tres entradas)
var_con_rep = function(n,p){
  return(n^p)
}
#permutations(n= 4, r= 3, v= x, repeats.allowed = TRUE)

# permutaciones cualquier orden (variaciones sin repetición)
# importa el orden de entrada y donde no se repiten los elementos
perm_con_orden <- function(n,r){
  return(factorial(n)/factorial(n-r))
}
#permutations(n= 5, r= 3, v=x, repeats.allowed = FALSE)

# combinaciones
# no se repiten los elementos (cada persona puede ser seleccionada una sola vez), 
# donde evidentemente no se seleccionan todos los elementos 
# (solo tres personas son las agraciadas para el premio) y donde no importa el orden 
# (es exactamente lo mismo que Pepito, Pepita y Pepete sean escogidos que lo sea Pepita, Pepito y Pepete o que lo sea Pepete, Pepito y Pepita)
perm_sin_orden <- function(n,r){
  return(fact(n)/(fact(n-r)*fact(r)))
}

#combinations(n=10, r=3, v=x)