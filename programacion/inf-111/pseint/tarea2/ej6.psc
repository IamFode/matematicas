Algoritmo ej6
	Leer min
	conv <- min*(1/60)*(1/24)*(1/365)
	a�o <- trunc(conv)
	p_d <- abs(conv)-abs(a�o)
	dias <- trunc(p_d*365)
	Escribir a�o,dias
FinAlgoritmo
