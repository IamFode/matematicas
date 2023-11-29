
load mit200

% Deteccion automatica de picos

    ... Descomposicion wavelet hasta nivel 5, y seleccionamos la banda de
    ... frecuencias sociadas a D4 y D5
        [C,L] = wavedec(ecgsig,5,'sym3');
        D4 = wrcoef('d',C,L,'sym3',4);
        D5 = wrcoef('d',C,L,'sym3',5);
        y=D4+D5;
        y=abs(y);
        plot(tm,y)
      
    ... Funcion de deteccion de picos, que implementamos sobre y:
        [qrspeaks1,locs1] = findpeaks(y,'MinPeakHeight',0.2,...
        'MinPeakDistance',20);
        locs1(1:5)
        ann(1:5)

        figure
        plot(tm,y)
        hold on
        plot(tm(locs1),qrspeaks1,'ro')
        xlabel("Segundos")
        title("Picos R wavelet notas")
        hold off
     
    ... Comparemos las posiciones detatadas automaticamente, con las de las 
    ... anotaciones de los cardiologos:
        figure
        plot(tm,ecgsig)
        hold on
        plot(tm(locs1),ecgsig(locs1),'ro')
        plot(tm(ann),ecgsig(ann),'k*')
        xlabel("Sgundos")
        title("Picos R wavelet notas y cardiologos")
        hold off