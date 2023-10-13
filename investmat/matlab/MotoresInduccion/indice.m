function indice(signal, nivel, wavelet, k)
    %% Paso 1: Obtenemos las señales de aproximacion y detalles: A8, D8.
    [C, L] = wavedec(signal, nivel, wavelet);
    A8 = wrcoef('a', C, L, wavelet, nivel);
    D8 = wrcoef('d', C, L, wavelet, nivel);

    %% Paso 2: Consideramos las diferencias en valor absoluto.
    difA8 = abs(A8(1:end-1) - A8(2:end));
    difD8 = abs(D8(1:end-1) - D8(2:end));

    %% Paso 3: Calcular las diferencias y aplicar la media móvil.
    VA8_i = medmov(difA8, k);
    VD8_i = medmov(difD8, k);
    
    %% Paso 4: Normalizamos para reducir efectos frontera.
    VA8mod_i = max(VA8_i, median(VA8_i));
    NVD8_i = VD8_i ./ VA8mod_i;
    
    % Encuentra el índice del valor máximo en NVD8_i
    [~, maxNVD8_i] = max(NVD8_i);
    
    indicador = 1000 * (VD8_i(maxNVD8_i) - VA8mod_i(maxNVD8_i));
    
    % Mostrar los valores como salida
    disp(inputname(1));
    disp(['Index: ', num2str(indicador)]);
    disp(['Position: ', num2str(maxNVD8_i)]);
end