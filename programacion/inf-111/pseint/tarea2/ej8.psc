Algoritmo ej8
	Leer n
	suma <- 0
	Mientras n<>0 Hacer
		ext <- n MOD 10
		suma <- suma+ext
		n <- trunc(n/10)
	FinMientras
	Escribir suma
FinAlgoritmo
