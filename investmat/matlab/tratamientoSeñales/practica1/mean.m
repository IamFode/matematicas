% EJEMPLO
    % Generar una señal con 1024 datos evaluados con la funcion 
    ...g(x) = 20*x^2*(1-x)^4*cos(12*pi*x)
    ...en el intervalo [0,1].
    x = 0:1/1023:1;
    signal = (20*x.^2).*((1-x).^4).*cos(12*pi*x);
    plot(signal); axis([0 1024 -0.5 0.5]);


% TRANSFORMADA DE HAAR
waveinfo('haar');

    % Coeficientes wavelets a nivel uno.
    [C,L] = wavedec(signal,1,'haar');

    % La orden necesita tres argumentos, el primero es la senal,
    ...el segundo los niveles de descomposicion y el tercero es la 
    ...wavelet a utilizar (en nuestro caso, Haar).
    a1 = appcoef(C,L,'haar',1); d1 = detcoef(C,L,1);

        % Plots
        subplot(1,2,1); plot(a1);
        title('Aproximacion'); axis([1 length(a1) -1 1]);
        subplot(1,2,2); plot(d1);
        title('Detalles'); axis([1 length(d1) -0.25 0.25]);
    
    % Para la aproximacion y detalles de primer nivel (A1 y D1)
    ls = length(signal); A1 = wrcoef('a',C,L,'haar',1);
    D1 = wrcoef('d',C,L,'haar',1); subplot(1,2,1); plot(A1);
    title('Aproximacion'); axis([1 ls -1 1]); subplot(1,2,2);
    plot(D1); title('Detalle'); axis([1 ls -0.1 0.1]);



% FUNCIONES CON MATLAB

    % cumenergy
    x = [1 2 3];
    [y] = cumenergy(x)

    % errorRMS
    [e] = errorRMS(x,y)

% APROXIMACION DE FUNCIONES
    
    % senal con 4096 datos evaluados con la funcion
    ...f(t)=20t^2(2-t)^5(4-t)^2cos(12pit)+30t^2(2-t)^2(4-t)^5cos(24pit)
    t=0:4/4095:4;
    y=(20*t.^2).*((2-t).^5).*((4-t).^2).*cos(12*pi*t)+...
    (30*t.^2).*((2-t).^2).*((4-t).^5).*cos(24*pi*t);
    y=y';
    plot(y);

    % Señal que contenga todas las diferencias en valor absoluto 
    ...entre terminos consecutivos.
    dify = abs(y(1:end-1)-y(2:end));
    plot(y);

    %estudio de variabilidad de la señal y a continuacion, 
    ...obteniendo el valor maximo de dicha variabilidad
    ...entre todas sus subsenales de longitud 100. Tomamos 
    ...como y una senal con 4096 datos evaluados con la funcion
    vary100 = medmov(dify,100);

    % Ejemplo de Variabilidad maxima y minima de y entre todas
    ...las subseñales de longitud 100:
    max(vary100)
    min(vary100)

    % Que nos da, respectivamente, 491.6340 y 0.1724. O tambien las
    ...posiciones (entradas iniciales) donde se dan las variabilidades
    ...maxima y minima:
    find(vary100>491.63)
    find(vary100<0.1725)
    find(vary100>=491.6340)
    find(vary100<=0.1724)
    

