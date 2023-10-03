function [e] = errorRMS(x,y)
% Obtiene el error RMS entre 2 se˜nales x e y.
% Las señales x e y deben tener la misma longitud.
e = sqrt(norm(x-y)^2/length(x));