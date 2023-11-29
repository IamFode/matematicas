% Plots
    ... s1
        plot(s1)
        waveletSignalAnalyzer

% Descomposicion    
    [C,L] = wavedec(s1,7,'coif5');
    D1 = wrcoef('d',C,L,'coif5',1);
    A7 = wrcoef('a',C,L,'coif5',7);
    plot(A7)

%   Plot cambio de signo
    cs = A7(1:end-1).*A7(2:end);
    pcs = find(cs<0);
    figure
    plot(A7)
    hold on
    plot(pcs,A7(pcs),'ro')
    hold off

% Desviacion estandar
    std(D1)
  