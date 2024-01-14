M1 = table2array(HICPM1(:,3));
HIPC = table2array(HICPM1(:,4));

wcoherence(M1,HIPC,years(1/12));


% Definir los datos
inflacion = HIPC % Tu vector de datos de inflación
crecimiento_dinero = M1 % Tu vector de datos de crecimiento del dinero

% Definir el número de términos en la serie de Fourier
n = length(inflacion); 

% Calcular la transformada de Fourier para la inflación
F_inflacion = fft(inflacion);
F_inflacion = F_inflacion(1:n/2); % Conservar solo la primera mitad

% Calcular la transformada de Fourier para el crecimiento del dinero
F_crecimiento_dinero = fft(crecimiento_dinero);
F_crecimiento_dinero = F_crecimiento_dinero(1:n/2); % Conservar solo la primera mitad

% Crear un vector de frecuencias (en ciclos por mes)
f = (0:n/2-1)/n;

% Graficar la serie de Fourier para la inflación
figure;
plot(f, abs(F_inflacion));
title('Serie de Fourier de la Inflación');
xlabel('Frecuencia (ciclos por mes)');

% Graficar la serie de Fourier para el crecimiento del dinero
figure;
plot(f, abs(F_crecimiento_dinero));
title('Serie de Fourier del Crecimiento del Dinero');
xlabel('Frecuencia (ciclos por mes)');


% Crear un modelo VAR
Mdl = varm(2,10); % 2 variables, retraso de 10

% Estimar los parámetros del modelo VAR
EstMdl = estimate(Mdl,[inflacion, crecimiento_dinero]);

% Realizar la prueba de causalidad de Granger
[h, pValue] = gctest(EstMdl, 'cause', 1, 'effect', 2);
