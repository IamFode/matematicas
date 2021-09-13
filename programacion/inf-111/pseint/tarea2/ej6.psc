Algoritmo ej6
	Leer min
	conv <- min*(1/60)*(1/24)*(1/365)
	año <- trunc(conv)
	p_d <- abs(conv)-abs(año)
	dias <- trunc(p_d*365)
	Escribir año,dias
FinAlgoritmo
