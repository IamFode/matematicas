######################### EJERCICIOS CAPÍTULO 1 ################################

## Datos sacados del INE de importaciones. PESO BRUTO (Kilogramos)
library(readxl)
library(fdth)
impor <- read_excel("/d/git/matematicas/estadistica/probabilidad/data/IMPORTACIONES ENE-SEP_2021p.xlsx")
x = impor$KILBRU
source("funciones.R")

####### 1.1. #######
dist <- fdt(impor$KILBRU, breaks = "Sturges", right = FALSE)
acum <- cumsum(x)
# a) frecuencia relativa
relativo <- prop.table(x)
# b) frecuencia relativa acumulada
relacum <- cumsum(relativo)
frec1 <- data.frame(x,acum,relativo,relacum)
# c) recorridos intercuantil e interdecil
quantile(frec1$relacum,.75)- quantile(frec1$relacum,.25)
IQR(frec1$relacum) 
quantile(frec1$relacum,.9)- quantile(frec1$relacum,.1)
# e) media, mediana, moda, desviación estándar con datos acumulados
mean(frec1$x)
median(frec1$x)
varianza(frec1$x)
var(frec1$x)*(length(x)-1)/length(x)
moda(frec1$x)
sd(frec1$x)
sqrt(varianza(frec1$x))

####### 1.2. #######
dem <- c(38,67,28,49,47,35,63,25,78,66,76,33,36,48,58,58,69,32,42,44,48,53,61,72,44,59,51,57,52,56)
# a) frecuencia relativa y de frecuencia acumulada
frecacum <- cumsum(dem)
relativ <- prop.table(dem)
frec2 <- data.frame(dem,frecacum,relativ)
# b) con distribución acumulada determine los tres cuantiles
quantile(frec$dem)

# c) media, mediana, moda, desviación estándar, desviación media y desviación mediana
# datos no agrupados
mean(dem)
median(dem)
moda(dem)
sd(dem)
DM(dem)
DMed(dem)

####### 1.3. #######
uno <- c(1,2,3,4,5,6)
dos <- c(1,1,1,6,6,6)
tres <- c(-13,2,3,4,5,20)
# calcular la media y la varianza
mean(uno)
varianza(uno)
mean(dos)
varianza(dos)
mean(tres)
varianza(tres)

####### 1.4. #######
venta_compu <- c(40.2,26.9,44.2,31.7,29.3,28.7,32.3,36.8,35.6,99.8,55.2,45.2,88.2,35.6,50.6,25.1,42.9,37.8,25.4,39.7) 
mean(venta_compu)
median(venta_compu)
varianza(venta_compu)
sqrt(varianza(venta_compu))
quantile(venta_compu)
quantile(venta_compu,.1)
quantile(venta_compu,.2)
quantile(venta_compu,.3)
quantile(venta_compu,.4)
quantile(venta_compu,.5)
quantile(venta_compu,.6)
quantile(venta_compu,.7)
quantile(venta_compu,.8)
quantile(venta_compu,.9)
quantile(venta_compu,.10)

####### 1.5 ########
transfor <- c()
for (i in frec2$dem) transfor <- c(transfor,(i-51.5) / 14.17)
frec2$transfor <- transfor
# a) frecuencia relativa
frec2$transfor_acum <- cumsum(frec2$transfor)
# b) media, desviación estándar
mean(frec2$transfor)
sqrt(varianza(frec2$transfor))

####### 1.6 #######

