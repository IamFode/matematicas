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


