########################## DISTRIBUCIÓN NORMAL #################################
# Función de densidad
func_normal = function(x,mu,sigma){
  return(1/(sqrt(2*pi)*sigma)*exp(-1/2*((x-mu)/sigma)^2))
}


