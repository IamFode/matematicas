Algoritmo ej9
	Leer año
	conv <- 365*24*60*60
	pob <- conv*((1/7)-(1/13)+(1/45))
	pob_total <- 312032486+(año*pob)
	Escribir redon(pob_total)
FinAlgoritmo
