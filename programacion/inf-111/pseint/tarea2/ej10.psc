Algoritmo ej10
	Leer total
	Leer pago
	c <- pago-total
	cambio <- c
	cinco <- trunc(cambio/5)
	cambio <- 5*(cambio/5-cinco)
	dos <- trunc(cambio/2)
	cambio <- 2*(cambio/2-dos)
	uno <- trunc(cambio)
	cambio <- cambio-uno
	cincuenta <- trunc(cambio/0.5)
	cambio <- 0.5*(cambio/0.5-cincuenta)
	veinte <- trunc(cambio/0.2)
	cambio <- 0.2*(cambio/0.2-veinte)
	diez <- trunc(cambio/0.1)
	Escribir c
	Escribir cinco
	Escribir dos
	Escribir uno
	Escribir cincuenta
	Escribir veinte
	Escribir diez
FinAlgoritmo
