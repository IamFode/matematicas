Algoritmo uno
	n <- 1
	count_menor <- 0
	count_mayor <- 0
	Mientras n<=5 Hacer
		Leer a
		Leer h
		sup <- a*h
		Si sup<=5.2 Entonces
			count_menor <- count_a+1
		SiNo
			count_mayor <- count_mayor+1
		FinSi
		n <- n+1
		Leer a
		Leer b
		sup <- a*b
	FinMientras
	Escribir count_mayor
	Escribir count_menor
FinAlgoritmo
