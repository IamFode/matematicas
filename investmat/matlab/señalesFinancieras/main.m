%% Deteccion de patrones en señales financieras
load('dat.mat');

    % Variables
    ... dia
    ... hora
    ... open
    ... max
    ... min
    ... close
    
    % Observemos el primero y ultimo dia de la data
    dat(1,1)
    dat(end,1)
    % Observamos las filas 1000 y 1001 con la columna 2
    dat(1000:1001,2)

    %% Realizaremos un analisis de patron bandera alcista y bajista
    ... Utilizaremos plantillas donde 1 toca las "velas" y 0 no lo toca
    ... help candle
    candle(dat(35:45,3:6))

    ... Cargaremos el patron bandera alcista (PB)  y el patron banera
    ... bajista o inverso (PBI):
    [PB,PBI] = Banderas;

    %% PASO 1
    ... En primer lugar vamos a determinar para cada tramo de 10 velas, con 
    ... inicio en la i.esima, el valor maximo, minimo (respecto los 20
    ... valores entre aperturas y cierres)
    Matriz{123}

    %% Posicion alcista perfecta
    alz = find(FVa==5);
    alz(1)
    candle(dat(16:25,3:6))
    
