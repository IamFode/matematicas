# library
library(ggplot2)

############################## Ejemplo 3.8 #####################################

# Funciones #

# r-esimo momento de X alrededor de cero
rmoment <- function(r,x,y){
  esp <- 0
  for (i in 1:length(x)){ 
    esp <- esp + ((x[i]^r)*y[i])
  }
  return(esp)
}

# r-ésimo momento central de X o momento alrededor de la media de X

rmomentc <- function(r,x,y){
  esp <- 0
  for (i in 1:length(x)){ 
    esp <- esp + ( (x[i]-rmoment(1,x,y))^r * y[i] )
  }
  return(esp)
}



momentosc <- function(r,x,y){
  sum <- 0
  for (i in 0:r){
    sum <- sum + ( (-1)^i*(factorial(r)/(factorial(r-i)*factorial(i))) * rmoment(1,x,y)^i * rmoment(r-i,x,y))
  }
  return(sum)
}


x <- data.frame(
  "x" = c(0,1,2,3,4,5,6,7,8),
  "p(x)" = c(0.02,0.09,0.21,0.28,0.23,0.12,0.04,0.01,0)
)

y <- data.frame(
  "y" = c(0,1,2,3,4,5,6,7,8,9,10,11,12),
  "p(y)" = c(0.06,0.21,0.28,0.24,0.13,0.05,0.02,0.01,0,0,0,0,0)
)

### variables x ###
rmoment(1,x$x,x$p.x.)
rmoment(2,x$x,x$p.x.)
rmoment(3,x$x,x$p.x.)
rmoment(4,x$x,x$p.x.)
#Var(X)
rmomentc(2,x$x,x$p.x.)
# u_3
momentosc(3,x$x,x$p.x.)
rmomentc(3,x$x,x$p.x.)
# tercer momento estadarizado
momentosc(3,x$x,x$p.x.) / (rmomentc(2,x$x,x$p.x.))^(3/2)
# cuarto momento estandarizado
momentosc(4,x$x,x$p.x.) / (rmomentc(2,x$x,x$p.x.))^2

### variable y  ###
rmoment(1,y$y,y$p.y.)
rmoment(2,y$y,y$p.y.)
rmoment(3,y$y,y$p.y.)
rmoment(4,y$y,y$p.y.)
#Var(X)
rmomentc(2,y$y,y$p.y.)
# u_3
momentosc(3,y$y,y$p.y.)
rmomentc(3,y$y,y$p.y.)
# u_4
rmomentc(4,y$y,y$p.y.)
# tercer momento estadarizado
alfa3 <- momentosc(3,y$y,y$p.y.) / (rmomentc(2,y$y,y$p.y.))^(3/2)
# cuarto momento estandarizado
alfa4 <- momentosc(4,y$y,y$p.y.) / (rmomentc(2,y$y,y$p.y.))^2

"
según el tercer momento el cual mide la simetría se tiene que Y es mas sesgado
que X hacia la derecha es decir u_3 > 0. Luego X es platicúrtica (alpha<3) e 
Y es letocúrtica alpha > 3
"

############################## Ejercicios #######################################

####### 3.1 #######
# a) 
X <- c(0,1,2,3,4,5,6,7)
fp <- c()
for (x in 0:7) {
  fp <- c(fp, exp(-3)*3^x / factorial(x))
}
df <- data.frame(X,fp,fda)

# b)
ggplot(data = df, mapping = aes(X,fp)) + 
  geom_col(width = 0.1)

# c)  
fda <- c()
sum <- 0
for (x in 0:7) {
  sum <- sum + (exp(-3)*3^x / factorial(x))
  fda <- c(fda,sum)
}

# d)
ggplot(data = df, mapping = aes(X,fda)) + 
  geom_line(width = 2)

####### 3.2 ######
