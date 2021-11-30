# definición 
"
Un estadístico o estimador puntual es una funcion que aplicada a una muestra nos
permite estimar un valor que queramos conocer sobre toda la población
"

# cuando hablemos de error estándar de T hablaremos de su desviación típica
# Generalmente 

############################ Media Muestral ####################################
# La media muestral estima la media poblacional mu
"
Ejercicio.
Cosideremos las tablas de datos iris. Vamos a comprobar las propiedades anterio-
res sobre la variable longitud de pétalo (Petal.Length)
1. Generaremos 10000 muestras de tamaño 40 con reposición de las longitudes del
   pétalo.
2. A continuación hallaremos los valores medios de cada muestra.
3. Consideraremos la media y la desviación típica de dichos valores medios y los 
   compararemos con los valores exctos dados por las propiedades de la media mues -
tral
"
set.seed(1001)
valores.medios.long.pétalo = replicate(10000, 
                                       mean(sample(iris$Petal.Length, 
                                                   40,
                                                   replace = TRUE)))
mean(valores.medios.long.pétalo)
mean(iris$Petal.Length)
#Desviación típica
sd(valores.medios.long.pétalo)
sd(iris$Petal.Length) / sqrt(40)
