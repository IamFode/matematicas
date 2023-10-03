function [y] = cumenergy(x)

% Obtiene el perfil de energia acumulado (y normalizado)
... de una señal x.
y = cumsum(x.^2) / (norm(x)^2);