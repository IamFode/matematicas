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
# a) recuencia relativa
relativo <- prop.table(x)
# b) frecuencia relativa acumulada
relacum <- cumsum(relativo)
frec <- data.frame(x,acum,relativo,relacum)
# c) recorridos intercuantil e interdecil
quantile(frec$relacum,.75)- quantile(frec$relacum,.25)
IQR(frec$relacum) 
quantile(frec$relacum,.9)- quantile(frec$relacum,.1)
# e) media, mediana, moda, desviación estándar con datos acumulados
mean(frec$x)
median(frec$x)
moda(frec$x)
sd(frec$x)

####### 1.2. #######
dem <- c(38,67,28,49,47,35,63,25,78,66,76,33,36,48,58,58,69,32,42,44,48,53,61,72,44,59,51,57,52,56)
# a) frecuencia relativa y de frecuencia acumulada
relativo <- prop.table(dem)
