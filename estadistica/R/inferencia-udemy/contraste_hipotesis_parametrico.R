
################################################################################
"Contraste de hipótesis para el parámetro mu de una variable normal con sigma 
conocida"
################################################################################

# Estadístico de contraste Z
Z = (function(media,mu,sigma,n) (media-mu)/(sigma/sqrt(n)))

# Alpha P(rechazar H_0 | H_0 cierta)
alpha = (function(Z) qnorm(Z)) 

# Alpha - 1
alpha_1 = (function(Z) qnorm(Z,lower.tail = TRUE))

# Rechazamos H_0 si media-mu/sigma/sqrt(n)>z_{1-alpha}
rechazo = (function(Z,alpha) 
          if (Z > 1-alpha) "Rechazamos H_0" 
          else "Aceptamos H_0")

# Intervalo de confianza mayor que
rechazoInterval = function(media,mu,sigma,n,alpha){
  I = media-(1-alpha)*sigma/sqrt{n}
  while(mu>=I){
    print("")
  }
}



