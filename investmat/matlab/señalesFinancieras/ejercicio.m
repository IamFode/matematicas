%% A) 
% Con todo lo anterior, hay que generar un unico script o funcion 
...en Matlab que:

    % 1 
    ...Genere las posiciones de FV, tanto bajista como alcista, para todos
    ...los valores entre 0 y 5.

    % 2 
    ... Obtenga el numero de operaciones a realizar si entraramos a operar
    ... bajistas, alcistas, y para cada valor de FV seleccionado.

    alz0 = find(FVa==0);
    alz1 = find(FVa==1);
    alz2 = find(FVa==2);
    alz3 = find(FVa==3);
    alz4 = find(FVa==4);
    alz5 = find(FVa==5);

    baj0 = find(FVb==0);
    baj1 = find(FVb==1);
    baj2 = find(FVb==2);
    baj3 = find(FVb==3);
    baj4 = find(FVb==4);
    baj5 = find(FVb==5);


%%B)
% Despues de correr el script o funcion sobre los datos, seleccionar 
... algunas posiciones (10, y para diferentes valores de FV) donde 
... entrariamos a operar y obtener el diagrama de 30 velas posterior a la 
... entrada, para comprobar graficamente si la “apuesta” era buena.

% Para FVa0
alz0(1)
candle(dat(681:711,3:6))

% Para FVa1
alz1(1)
candle(dat(63:103,3:6))

% Para FVa2
alz2(1)
candle(dat(171:211,3:6))

% Para FVa3
alz3(1)
candle(dat(829:869,3:6))

% Para FVa4
alz4(1)
candle(dat(1880:1910,3:6))

% Para FVa5
alz5(1)
candle(dat(16:46,3:6))

% Para FVb0
baj0(1)
candle(dat(294:324,3:6))

% Para FVb1
baj1(1)
candle(dat(89:109,3:6))

% Para FVb2
baj2(1)
candle(dat(88:108,3:6))

% Para FVb3
baj3(1)
candle(dat(1234:1264,3:6))

% Para FVb4
baj4(1)
candle(dat(3:43,3:6))

% Para FVb5
baj5(1)
candle(dat(295:325,3:6))