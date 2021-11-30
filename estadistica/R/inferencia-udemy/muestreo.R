# librerías
library(faraway)

#################### Conceptos básicos de muestreo #############################
  ## Establecer la característica que se desea estimar o la hipótesis que desea 
    # contrastar
  ## Determinar la información es decir los datos que se necesita para hacerlo.
  ## Diseñar un experimento que permita recoger estos datos; este paso incluye:
    ### Decidir qué tipo de muestra se va a tomar y su tamaño
    ### Elegir las técnicas adecuadas para realizar las inferencias deseadas a 
        # partir de la muestra que se tomará


################ Muestro aleatorio con y sin reposición ########################

### Muestra aleatorio simple o con repocisión 
"
 Para simular un muestreo de 15 bolas con repocisión en una urna de 100 en R 
haríamos lo siguiente
"
sample(1:100, 15, replace = TRUE)
## iris
head(iris)
# muestra de 10 flores con repocisión 
set.seed(4)
flores.elegidas.10.con = sample(1:150,10,replace = TRUE)
muestra.iris.10.con = iris[flores.elegidas.10.con,]
### Muestreo simple sin reposición
sample(1:100,15,replace = FALSE)
set.seed(4)
flores.elegidas.10.sin = sample(1:150,10,replace = FALSE)
muestra.iris.10.sin = iris[flores.elegidas.10.sin,]
"
Es lo mismo muestras aleatorias con repocisión o sin repocisión siempre y cuando 
el tamaño de la población sea muy grande en realación de la muestra. 
Unas 1000 veces por mayor
"

##################### Muestreo aleatorio sistemático ###########################
"
Consiste en tomarlos a intervalos constantes escogiendo al azar el primer 
individuo que elijamos
"
set.seed(15)
(primera.flor=sample(1:150,1))
incremento = floor(150/10) # incremento
flores.elegidas.10.sis = seq(from = primera.flor, by = incremento, length.out=10)
flores.elegidas.10.sis = flores.elegidas.10.sis %% 150
muestra.iris.10.sis = iris[flores.elegidas.10.sis,]

##################### Muestreo aleatorio estratificado #########################
"
Consiste en tomar una proporción justa de entre dos partes, por ejemplo se tiene 
10 hombres y 5 mujeres por lo tanto se toma una proporción 5/10 de los cuales se 
toma la mitad de muestras de mujeres de los que se tomaría para las hombres.
"
set.seed(25)
fls.muestra.setosa = sample(1:50,4,replace = TRUE)
fls.muestra.versicolor = sample(51:100,4,replace = TRUE)
fls.muestra.virginica = sample(101,150,replace = TRUE)
(muestra.iris.est = rbind(iris[fls.muestra.setosa,],
                          iris[fls.muestra.versicolor,],
                          iris[fls.muestra.virginica,]))

########################### Muestreo por conglomerado ##########################
"
En vez de extraer una muestra aleatoria de todos los individuos de la población
escoger primero al azar unos subconjuntos en los que la población está dividida
a las que llamamos en este contexto conglomerado (clusters).
Por ejemplo se tiene 20 edificios de 5 pisos cada uno, para no ir a todos los 
edificios se toma 4 edificios al azar de los cuales se sacará muestras.
"
head(worldcup)
"
Supongamos que queremos calcular una muestra de tamaño indeterminado de los ju -
gadors por conglomerados eligiendo como conglomerados los países a los que éstos
pertenecen.
Elijamos primero 4 países aleatoriamente de los 32 países y la muestra elegida 
serán los jugadores que pertenecen a dichos países:
"
set.seed(19)
números.paises.elegidos = sample(1:32, 4, replace = FALSE)
paises.elegidos = unique(worldcup$Team)[números.paises.elegidos]
paises.elegidos
"
La muestra elegida estará formada por los jugadores que pertenecen a dichos pa -
ises
"
muestra.worldcup.con = worldcup[worldcup$Team%in%paises.elegidos,]
head(muestra.worldcup.con,8)


########################### Muestreo polietápico ###############################
"
Si una vez seleccionada la muestra aleatoria de conglomerados, tomamos de alguna
manera una muestra aleatoria de cada uno de ellos.
Por ejemplo hemos elegido al azar 5 conglomerados y de cada uno de ellos hemos 
elegido 3 al azar sin respetición.
Para realizar un muestreo con los datos del ejemplo anterior, podemos elegir una
submuestra de 5 jugadores para cada uno de los 4 países elegidos, obteniendo al 
final una muestra de tamaño 20 de todos los jugadores de la tabla de datos.
Primero definimos las 4 subtablas de datos para los jugadores de cada país ele -
gido.
"
worldcup.pais1 = worldcup[worldcup$Team==paises.elegidos[1],] 
worldcup.pais2 = worldcup[worldcup$Team==paises.elegidos[2],] 
worldcup.pais3 = worldcup[worldcup$Team==paises.elegidos[3],] 
worldcup.pais4 = worldcup[worldcup$Team==paises.elegidos[4],] 
set.seed(28)
jugadores.pais1 = sample(1:dim(worldcup.pais1)[1], 5, replace = FALSE)
jugadores.pais2 = sample(1:dim(worldcup.pais2)[1], 5, replace = FALSE)
jugadores.pais3 = sample(1:dim(worldcup.pais3)[1], 5, replace = FALSE)
jugadores.pais4 = sample(1:dim(worldcup.pais4)[1], 5, replace = FALSE)
muestra.worldcup.pol = rbind(worldcup.pais1[jugadores.pais1,],
                             worldcup.pais2[jugadores.pais2,],
                             worldcup.pais3[jugadores.pais3,],
                             worldcup.pais4[jugadores.pais4,])
head(muestra.worldcup.pol,12)
# sample(x, n , replace = ...)





