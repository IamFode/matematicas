load mit200
plot(ecgsig)


% Plot de seal ECG en el intervalo de tiempo:
plot(tm,ecgsig)
xlabel("Segundo")
ylabel("Amplitud")


% Anotaciones de cardiologos.
figure
plot(tm,ecgsig)
hold on
plot(tm(ann),ecgsig(ann),"ro")
xlabel("Segundos")
ylabel("Amplitud")
title("Muestra - MIT-BIH 200")
hold off


% Deteccion automatica de picos

    ... Descomposicion wavelet hasta nivel 5, y seleccionamos la banda de
    ... frecuencias sociadas a D4 y D5
        [C,L] = wavedec(ecgsig,5,'sym4');
        D4 = wrcoef('d',C,L,'sym4',4);
        D5 = wrcoef('d',C,L,'sym4',5);
        y=D4+D5;
        y=abs(y);
        plot(tm,y)
      
    ... Funcion de deteccion de picos, que implementamos sobre y:
        [qrspeaks,locs] = findpeaks(y,'MinPeakHeight',0.4,...
        'MinPeakDistance',54);
        locs(1:5)
        ann(1:5)

        figure
        plot(tm,y)
        hold on
        plot(tm(locs),qrspeaks,'ro')
        xlabel("Segundos")
        title("Picos R wavelet notas")
        hold off
     
    ... Comparemos las posiciones detatadas automaticamente, con las de las 
    ... anotaciones de los cardiologos:
        figure
        plot(tm,ecgsig)
        hold on
        plot(tm(locs),ecgsig(locs),'ro')
        plot(tm(ann),ecgsig(ann),'k*')
        xlabel("Sgundos")
        title("Picos R wavelet notas y cardiologos")
        hold off

% Analizador Wavelet
signalMultiresolutionAnalyzer
waveletSignalAnalyzer
waveletSignalDenoiser
waveletTimeFrequencyAnalyzer

        